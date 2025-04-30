import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import warnings
warnings.filterwarnings("ignore")
import requests
from bs4 import BeautifulSoup

# --- 설정 ---
# 사용할 Gemma 모델 ID (Instruction-Tuned 버전 권장)
MODEL_ID = "google/gemma-3-1b-it"  # 더 작은 모델로 변경 (GPU 사양 고려)
# 생성할 최대 토큰 수
MAX_NEW_TOKENS = 512


# 웹 검색 API 키 (본인의 API 키로 변경)
GOOGLE_SEARCH_API_KEY = "YOUR_GOOGLE_SEARCH_API_KEY"
GOOGLE_SEARCH_ENGINE_ID = "YOUR_GOOGLE_SEARCH_ENGINE_ID"  # 검색 엔진 ID



TOKEN = "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"

# --- 전역 변수 (모델/토크나이저 캐싱용) ---
model = None
tokenizer = None
model_device = None


def _load_gemma_model():
    """Gemma 모델과 토크나이저를 로드 (필요한 경우)."""
    global model, tokenizer, model_device
    if model is not None and tokenizer is not None:
        return True
    

    # 토크나이저 로드
    try:
        # token=True 또는 환경 변수 HUGGING_FACE_HUB_TOKEN 설정 필요할 수 있음
        tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, token=TOKEN)  # 필요시 token=True 추가
    except Exception as e:
        print("겜마로드드", e)
        return False

    # 모델 로드
    try:
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_ID,
            device_map="auto",  # 자동으로 GPU/CPU 할당
            torch_dtype=torch.float16, # 메모리 최적화
            token=TOKEN,
            low_cpu_mem_usage=True,
        )

        model_device = next(model.parameters()).device  # 모델이 로드된 실제 장치 확인
    except Exception as e:
        print("겜마로드드드드", e)
        # 실패 시 전역 변수 초기화
        model = None
        tokenizer = None
        model_device = None
        return False

    return True


def google_search(query, api_key, engine_id, num_results=3):
    """Google Custom Search API를 사용하여 검색 결과를 가져옵니다."""
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": engine_id,
        "num": num_results,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # HTTP 에러 처리
        results = response.json()
        return results
    except requests.exceptions.RequestException as e:
        print(f"❌ 웹 검색 오류: {e}")
        return None


def extract_text_from_url(url):
    """주어진 URL에서 텍스트 콘텐츠를 추출합니다."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text(separator=" ", strip=True)  # 모든 텍스트 추출 및 공백으로 분리
        return text
    except requests.exceptions.RequestException as e:
        print(f"❌ URL 텍스트 추출 오류: {e}")
        return None


def explain_food_gemma(food_name, exp_type):
    """
    주어진 음식 이름에 대해 Gemma 모델을 사용하여 설명을 생성합니다.
    웹 검색을 통해 얻은 정보를 활용하여 설명의 신뢰성을 높입니다.

    Args:
        food_name (str): 설명할 음식의 이름.
        exp_type (str): 설명 유형 (예: "일반적으로 들어가는 재료", "영양 정보").

    Returns:
        str: Gemma 모델이 생성한 음식 설명 텍스트, 또는 오류 메시지.
    """
    global model, tokenizer, model_device

    # 모델/토크나이저가 로드되지 않았으면 로드 시도
    if model is None or tokenizer is None:
        if not _load_gemma_model():
            return "오류: Gemma 모델을 로드할 수 없습니다."

    # 웹 검색을 통해 관련 정보 수집
    search_query = f"{food_name} {exp_type}"
    search_results = google_search(
        search_query, GOOGLE_SEARCH_API_KEY, GOOGLE_SEARCH_ENGINE_ID
    )

    context_text = ""
    if search_results and "items" in search_results:
        for item in search_results["items"]:
            url = item["link"]
            extracted_text = extract_text_from_url(url)
            if extracted_text:
                context_text += extracted_text[:500] + " "  # 텍스트 일부만 사용

    if exp_type == '일반적으로 들어가는 재료(뭘로 만들었는지)(단어 나열식으로)':
        # Gemma Instruction-Tuned 모델에 맞는 프롬프트 형식 생성
        prompt_text = f"""
        다음 정보를 참고하여 '{food_name}'에 대해 {exp_type}에 대해 알려줘 다른거 추가하지 말고 그냥 엔터로만 구분해줘. 그 외에는 따로 내용 추가하지 않아도 괜찮아:
        {context_text}
        """
    else:
        # Gemma Instruction-Tuned 모델에 맞는 프롬프트 형식 생성
        prompt_text = f"""
        다음 정보를 참고하여 '{food_name}'에 대해 {exp_type}에 대해서 2문장 정도로로 문단으로 구성해서 설명해줘 그 외에는 따로 내용 추가하지 않아도 괜찮아아:
        {context_text}
        """

    chat = [{"role": "user", "content": prompt_text}]
    # 채팅 템플릿 적용 (모델 입력 형식으로 변환)
    gemma_prompt = tokenizer.apply_chat_template(
        chat, tokenize=False, add_generation_prompt=True
    )

    inputs = tokenizer(gemma_prompt, return_tensors="pt").to(model_device)

    # 텍스트 생성
    try:
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )

        explanation = tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[1] :], skip_special_tokens=True
        ).strip()
        return explanation
    except Exception as e:
        print(f"❌ 텍스트 생성 중 에러: {e}")
        return f"'{food_name}'에 대한 설명을 생성하는 중 오류가 발생했습니다."


if __name__ == "__main__":
    # 프로그램 시작 시 모델 로딩 시도
    if _load_gemma_model():
        # 로딩 성공 시 테스트 실행
        food_to_explain = "김치찌개"
        explanation_type = "일반적으로 들어가는 재료(뭘로 만들었는지)(단어 나열식으로)" #or "영양 정보"
        explanation_result = explain_food_gemma(food_to_explain,explanation_type)

        print(explanation_result)
    else:
        print("오류: 모델 로딩에 실패하여 테스트를 실행할 수 없습니다.")