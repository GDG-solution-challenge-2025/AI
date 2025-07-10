from Menu_models.menu_recognition import recognize_menu
from Food_models.food_explanation_gemini import explain_food_gemini # Gemma 버전 함수 임포트
from Food_models.gemini_translation import trans_kor, trans_eng
import sys
import io
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

food_name = input()     #소갈비

food_info = input()     # 소고기, 콩

try:
    explanation=''
    translation = ''
    food_list = ''
    if food_name:
        food_kor = trans_kor(food_name)
        food_eng = trans_eng(food_name)
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
        print(food_kor+ '\n`---___###@@@\n'+ food_eng+'\n`---___###@@@\n'+ '\n' + explanation + '\n' + translation)

except Exception as e:
    print(f"처리 중 오류가 발생했습니다: {e}")
