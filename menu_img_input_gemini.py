from Menu_models.menu_recognition import recognize_menu
from Food_models.food_explanation_gemini import explain_food_gemini # Gemma 버전 함수 임포트
from Food_models.gemini_translation import trans_kor, trans_eng
import sys
import io
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
# C:\Users\Administrator\Desktop\dev\AI\menu.jpg


image_path = input()

#못먹는 음식식 정보 input
# food_info = input()

try:
    menu = recognize_menu(image_path)     #gemini data

except FileNotFoundError:
    print(f"오류: 이미지 파일({image_path})을 찾을 수 없습니다. 경로를 확인하세요.")
except Exception as e:
    print(f"처리 중 오류가 발생했습니다: {e}")



food = menu.split('\n`---___###@@@\n')  # 음식 리스트 생성
