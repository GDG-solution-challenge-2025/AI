# gemma hugginface access token
#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



import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import warnings
import sys
sys.stdout.reconfigure(encoding='utf-8')
warnings.filterwarnings("ignore")

# --- 설정 ---
# 사용할 Gemma 모델 ID (Instruction-Tuned 버전 권장)
#MODEL_ID = "google/gemma-7b-it"
MODEL_ID = "google/gemma-3-1b-it"
USE_4BIT_QUANTIZATION = False
# 생성할 최대 토큰 수
MAX_NEW_TOKENS = 512


# --- 전역 변수 (모델/토크나이저 캐싱용) ---
model = None
tokenizer = None
model_device = None

TOKEN = "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"

def _load_gemma_model():
    """Gemma 모델과 토크나이저를 로드 (필요한 경우)."""
    global model, tokenizer, model_device
    if model is not None and tokenizer is not None:
        return True


    quantization_config = None
    if USE_4BIT_QUANTIZATION:
        try:
            import bitsandbytes # bitsandbytes 임포트 시도
            quantization_config = BitsAndBytesConfig(load_in_4bit=True)
        except ImportError:
            print("겜마로드",e)
            return False

    # 토크나이저 로드
    try:
        # token=True 또는 환경 변수 HUGGING_FACE_HUB_TOKEN 설정 필요할 수 있음
        tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, token=TOKEN) # 필요시 token=True 추가
    except Exception as e:
        print("겜마로드드",e)
        return False

    # 모델 로드
    try:
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_ID,
            device_map="cpu", # 자동으로 GPU/CPU 할당
            #torch_dtype=torch.bfloat16,
            torch_dtype=torch.float32, 
            token=TOKEN,
            low_cpu_mem_usage=False,
        )

        model_device = next(model.parameters()).device # 모델이 로드된 실제 장치 확인
    except Exception as e:
        print("겜마로드드드드",e)
        # 실패 시 전역 변수 초기화
        model = None
        tokenizer = None
        model_device = None
        return False

    return True

def explain_food_gemma(food_name, exp_type, food_info, food_list):
    """
    주어진 음식 이름에 대해 Gemma 모델을 사용하여 설명을 생성합니다.

    Args:
        food_name (str): 설명할 음식의 이름.

    Returns:
        str: Gemma 모델이 생성한 음식 설명 텍스트, 또는 오류 메시지.
    """
    global model, tokenizer, model_device

    # 모델/토크나이저가 로드되지 않았으면 로드 시도
    if model is None or tokenizer is None:
        if not _load_gemma_model():
            return "오류: Gemma 모델을 로드할 수 없습니다."
    
    #exp_type = ['어떤 맛인지','유래','먹는 방법', '일반적으로 들어가는 재료', '1']

    if exp_type == '어떤 맛인지':
        prompt_text = f"""
        '{food_name}'이 {exp_type}에 대해서 다른 설명 없이 딱 2~3문장정도로 간단히 알려줘:
        """
    elif exp_type == '유래':
        prompt_text = f"""Please briefly describe the origin of the dish '{food_name}' in only 2-3 sentences.
        If you are not sure about the exact origin, just say 'The origin is unclear.'"""

    elif exp_type == '먹는 방법':
        prompt_text = f"""How is the dish '{food_name}' typically eaten? For example, is it eaten with rice, soup, or as a side dish? Briefly describe it in 2-3 sentences."""

    elif exp_type == '일반적으로 들어가는 재료':
        prompt_text = f"""List the typical ingredients used in '{food_name}' as one word per line. Do not include any explanations, formatting, or numbering."""

    else:
        # 5번: 못 먹는 음식과의 매칭 확인
        prompt_text = f"""
        The dish '{food_name}' contains the following ingredients:
        {food_list}

        The user cannot eat the following due to allergies or restrictions:
        {food_info}

        Check and list any ingredients (or their base components, e.g., tofu → soy) that match the restricted items.
        Output only the matched ones, one per line. If none match, write 'None'.
        """

    chat = [
        {"role": "user", "content": prompt_text}
    ]
    # 채팅 템플릿 적용 (모델 입력 형식으로 변환)
    gemma_prompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)

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

        explanation = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()
        return explanation
    except Exception as e:
        print(f"❌ 텍스트 생성 중 에러: {e}")
        return f"'{food_name}'에 대한 설명을 생성하는 중 오류가 발생했습니다."


# if __name__ == "__main__":
#     # 프로그램 시작 시 모델 로딩 시도
#     if _load_gemma_model():
#         # 로딩 성공 시 테스트 실행
#         food_to_explain = "김치찌개"
#         explanation_result = explain_food_gemma(food_to_explain)


#         print(explanation_result)
#     else:
#         print("오류: 모델 로딩에 실패하여 테스트를 실행할 수 없습니다.")
