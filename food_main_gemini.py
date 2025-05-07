from Food_models.food_recognition import recognize_food
from Food_models.food_explanation_gemini import explain_food_gemini # Gemma 버전 함수 임포트
from Food_models.gemini_translation import trans_kor, trans_eng
import warnings
import sys
sys.stdout.reconfigure(encoding='utf-8')
warnings.filterwarnings("ignore")

# C:\Users\kim1g\OneDrive\바탕 화면\GCU\sollution_challenge_git\AI\kc.jpeg

# 이미지 파일 경로
image_path = input()
# print(image_path)
# 땅콩, 
#못먹는 음식식 정보 input
food_info = input()

try:
    # 1단계: 음식 인식 (Gemini Vision 사용) 

    food_name = recognize_food(image_path)            # gemini 답변
    explanation=''
    translation = ''
    food_list = ''

    if food_name:
        exp_type = ['어떤 맛인지','유래','먹는 방법', '일반적으로 들어가는 재료', '1']
        for ex in exp_type:
            if ex == '일반적으로 들어가는 재료':
                expl = explain_food_gemini(food_name, ex, food_info, food_list)
                food_list = expl
                trans = trans_eng(expl)
                expl += '\n`---___###@@@\n'
                trans += '\n`---___###@@@\n'
                explanation += expl
                translation += trans
            else:
                expl = explain_food_gemini(food_name, ex, food_info, food_list)
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