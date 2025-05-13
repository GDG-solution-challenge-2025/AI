import google.generativeai as genai
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

# Gemini API 키 설정 (필요 시 변경)
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except Exception as e:
    print(f"Gemini API 키 설정 오류: {e}")
    exit()

# 설명 생성 함수
def explain_food_gemini(food_name, exp_type, food_info, food_list):
    model = genai.GenerativeModel('gemini-1.5-flash')

    # 1~4번까지 프롬프트 구성
    if exp_type == '어떤 맛인지':
        prompt = f"""
        '{food_name}'이 무슨 맛인지 알려줘. 한국어로 간단하게 2문장 정도로 설명해줘.
        """
        #What does '{food_name}' taste like? Please answer briefly in 2-3 sentences.
        
    elif exp_type == '유래':
        prompt = f"""
        '{food_name}'의 유래가 뭐야? 한국어로 간단하게 2문장 정도로 설명해줘. 만약 확실하지 않다면 그냥 '유래가 확실하지 않습니다'라고 답해줘.
        """
        #What is the origin of '{food_name}'? If you're not sure, simply say "The origin is unclear." Keep it brief and answer briefly in 2~3 sentences .
        
    elif exp_type == '먹는 방법':
        prompt = f"""
        '{food_name}'은 일반적으로 어떻게 먹어?(e.g., 밥과 함께, 국처럼, 반찬처럼 ..). 레시피를 알려달라는게 아니야. 답변은 2~3문장정도로 한국어로 간단한 문장으로 설명해줘.
        """
        #How is '{food_name}' typically eaten? (e.g., with rice, as soup, or side dish). Avoid giving recipes. Answer in 2-3 short sentences.
        
    elif exp_type == '일반적으로 들어가는 재료':
        prompt = f"""
        '{food_name}'에 들어가는 일반적인 음식 재료를 한국어로 알려줘. 추가 설명 필요없고 재료들은 각각 엔터로 구분해서 줘.
        """
        #List the typical ingredients used in '{food_name}', one per line with no explanations or formatting.
        
    else:
        # 5번: 못 먹는 음식과의 매칭 확인
        prompt = f"""
        '{food_name}'이 다음 재료를 포함하고 있어:
        {food_list}
        
        사용자가 다음 음식에 대해서 알레르기, 또는 섭취에 대한 제한이 있어:
        {food_info}

        제한 항목과 일치하는 재료(또는 그 기본 구성 요소, 예: 두부 → 콩)를 확인하고 같은 줄에 제한 항목과 일치하는 재료를 한국어로 작성하여 나열하세요.
        일치하는 항목만 한 줄에 하나씩 출력하세요. 일치하는 항목이 없으면 '없음'이라고 작성하세요.
        """
        # The dish '{food_name}' contains the following ingredients:
        # {food_list}

        # The user cannot eat the following due to allergies or restrictions:
        # {food_info}

        # Check and list any ingredients (or their base components, e.g., tofu → soy) that match the restricted items.
        # Output only the matched ones, one per line. If none match, write 'None'.

    # Gemini API 호출
    try:
        response = model.generate_content(prompt)
        result = response.text.strip()
        return result
    except Exception as e:
        print(f"❌ 설명 생성 중 오류 발생: {e}")
        return f"{food_name}에 대한 설명 생성 실패\n"
