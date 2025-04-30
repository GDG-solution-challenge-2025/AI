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


def recognize_menu(image_path):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    image = Image.open(image_path)

    prompt = """
    이 메뉴판의 음식 텍스트들을 모두 추출해서 엔터로 구분해서 줘 한국어로 된 메뉴만 한국어로 추출해줘 그리고 추출한 메뉴를 영어로 번역해서 그 밑에 같은 형식으로 출력해줘줘:
    """
    response = model.generate_content([prompt, image])

    food_name = response.text.strip()
    food_kor= food_name.split('\n\n')[0]
    food_eng= food_name.split('\n\n')[1]
    food_kor = food_kor.replace('\n','\n`---___###@@@\n')
    food_eng = food_eng.replace('\n','\n`---___###@@@\n')

    food = food_kor + '\n@@ko/eng@@\n'+ food_eng
    print(f"{food}")
    return food



# def fake_recognize(image_path):
#     food_name='영어: Tteokbokki\n한국어: 떡볶이'
#     return food_name
