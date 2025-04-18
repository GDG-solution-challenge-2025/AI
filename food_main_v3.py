from Food_models.food_recognition import recognize_food
from Food_models.food_explanation_gemma import explain_food_gemma # Gemma 버전 함수 임포트
from Food_models.gemma_translation import trans_eng
import warnings
warnings.filterwarnings("ignore")

# 테스트할 이미지 경로
image_path = input("파일 경로: ")
# print(image_path)

try:
    # 1단계: 음식 인식 (Gemini Vision 사용)         food_name 주석처리로 바꿔가며 사용용

    food_name = recognize_food(image_path)            # gemini 답변

    if food_name:
        # 2단계: 음식 설명 (Gemma 사용)
        explanation = explain_food_gemma(food_name)
        translation = trans_eng(explanation)
        print(explanation)
        print(translation)

        

except FileNotFoundError:
    print(f"오류: 이미지 파일({image_path})을 찾을 수 없습니다. 경로를 확인하세요.")
except Exception as e:
    print(f"처리 중 오류가 발생했습니다: {e}")