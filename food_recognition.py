import google.generativeai as genai
from PIL import Image

try:
    genai.configure(api_key="AIzaSyB_ysaob2As98H5g6WaeKSzS8QFtLUZeiA")
except ValueError as e:
    print(e)
    exit()
except Exception as e:
    print(f"API 키 설정 중 오류 발생: {e}")
    exit()


def recognize_food(image_path):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    image = Image.open(image_path)

    prompt = """
    이 음식의 이름이 뭐야? 영어, 한국어로 각각 간단하게 하나의 단어로 알려줘.

    형식은 아래 예시처럼 출력해줘:

    예시:
    떡볶이
    Tteokbokki
    """
    response = model.generate_content([prompt, image])

    food_name = response.text.strip()
    print(f"{food_name}")
    return food_name



# def fake_recognize(image_path):
#     food_name='영어: Tteokbokki\n한국어: 떡볶이'
#     return food_name
