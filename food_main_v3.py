from Food_models.food_recognition import recognize_food
from Food_models.food_explanation_gemma import explain_food_gemma # Gemma 버전 함수 임포트
from Food_models.gemma_translation import trans_eng
import warnings
warnings.filterwarnings("ignore")

# C:\Users\kim1g\OneDrive\바탕 화면\GCU\sollution_challenge_git\AI\kc.jpeg

# 이미지 경로
image_path = input("파일 경로: ")
# print(image_path)

try:
    # 1단계: 음식 인식 (Gemini Vision 사용) 

    food_name = recognize_food(image_path)            # gemini 답변
    explanation=''
    translation = ''
    if food_name:
        # 2단계: 음식 설명 (Gemma 사용)
        exp_type = ['어떤 맛인지','유래(모르면 그냥 확실하지 않다고 답변)','먹는 방법', '일반적으로 들어가는 재료(단어 나열식으로)']
        for ex in exp_type:
            expl = explain_food_gemma(food_name, ex)
            trans = trans_eng(expl)
            expl += '\n`---___###@@@\n'
            trans += '\n`---___###@@@\n'
            explanation += expl
            translation += trans
        print(explanation)
        print(translation)

        

except FileNotFoundError:
    print(f"오류: 이미지 파일({image_path})을 찾을 수 없습니다. 경로를 확인하세요.")
except Exception as e:
    print(f"처리 중 오류가 발생했습니다: {e}")