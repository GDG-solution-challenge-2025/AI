from Menu_models.menu_recognition import recognize_menu
from Food_models.food_explanation_gemma import explain_food_gemma # Gemma 버전 함수 임포트
from Food_models.gemma_translation import trans_eng

# C:\Users\kim1g\OneDrive\바탕 화면\GCU\sollution_challenge_git\AI\menu.png


image_path = input('파일 경로:' )


try:
    # 1단계: 음식 인식 (Gemini Vision 사용)
    menu = recognize_menu(image_path)     #gemini data

except FileNotFoundError:
    print(f"오류: 이미지 파일({image_path})을 찾을 수 없습니다. 경로를 확인하세요.")
except Exception as e:
    print(f"처리 중 오류가 발생했습니다: {e}")



food = menu.split('\n')  # 음식 리스트 생성

while True:
    input_food_name = input("음식 이름: ")      #백엔드에서 음식이름 입력력
    if input_food_name in food:
        food_name = input_food_name
        break
    else:
        print('Error: Invalid food name!!')

    

try:

    if food_name:
        # 2단계: 음식 설명 (Gemma 사용)
        explanation = explain_food_gemma(food_name)
        translation = trans_eng(explanation)
        print(explanation)
        print(translation)

except Exception as e:
    print(f"처리 중 오류가 발생했습니다: {e}")
