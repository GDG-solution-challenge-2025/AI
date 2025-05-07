import google.generativeai as genai
import sys
sys.stdout.reconfigure(encoding='utf-8')

try:
    genai.configure(api_key="AIzaSyADqOTHtn4yoEQOzPg_TQiZxdVhfcKeZSY")
except ValueError as e:
    print(e)
    exit()
except Exception as e:
    print(f"API 키 설정 중 오류 발생: {e}")
    exit()


def trans_kor(explanation):
    model = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"""
    '{explanation}'
    
    이 글을 한글로 그대로 번역해줘. 다른 말 추가하지 말고 번역한 글만 줘줘
    """
    response = model.generate_content([prompt])

    expl = response.text.strip()
    
    return expl

def trans_eng(explanation):
    model = genai.GenerativeModel('gemini-2.0-flash')

    prompt = f"""
    '{explanation}'
    
    이 글을 영어로 그대로 번역해줘. 다른 말 추가하지 말고 번역한 글만 줘줘
    """
    response = model.generate_content([prompt])

    expl = response.text.strip()
    
    return expl



# def fake_recognize(image_path):
#     food_name='영어: Tteokbokki\n한국어: 떡볶이'
#     return food_name
