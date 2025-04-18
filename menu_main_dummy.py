#dummy


from Menu_models.menu_recognition import recognize_menu
from Food_models.food_explanation_gemma import explain_food_gemma # Gemma 버전 함수 임포트
from Food_models.gemma_translation import trans_eng

# C:\Users\kim1g\OneDrive\바탕 화면\GCU\sollution_challenge_git\AI\menu.png


image_path = input('파일 경로:' )


menu = '김치찌개\n떡볶이\n김밥\n\nkimchijjigae\ntteokbbokki\ngimbap'     #dummy data

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
        explanation = "김치찌개는 한국의 대표적인 찌개 요리로, 매콤하면서도 시원한 맛이 특징입니다. 묵은지를 주재료로 하여 깊은 맛과 함께 밥과 함께 먹기 좋습니다. \n\n김치찌개는 한국의 전통적인 음식으로, 17세기 말부터 시작된 것으로 추정됩니다. 당시에는 김치와 돼지고기가 함께 먹는 풍습이 있었고, 이를 바탕으로 김치찌개의 기본적인 맛이 형성되었습니다.\n\n김치찌개는 다양한 재료를 활용하여 만들 수 있으며, 밥과 함께 먹으면 더욱 맛있습니다.\n\n묵은지\n돼지고기 (목살, 삼겹살 등)\n두부\n양파\n대파\n청양고추 (선택 사항)\n멸치\n다시마\n고사리 (선택 사항)"
        translation = "Kimchi stew is a quintessential Korean stew, known for its spicy and refreshing flavor. It's a staple for serving with rice, and it's a dish that's particularly delicious when enjoyed with rice.\n\nKimchi stew has been a traditional Korean dish since the 17th century, with its origins traced back to the late 18th century. During that time, a custom of eating kimchi and pork together was prevalent, which significantly shaped the basic flavor of kimchi stew.\n\nYou can use a variety of ingredients to make kimchi stew, and it tastes even better when served with rice.\n\nKimchi\nPork (such as pork belly or pork shoulder)\nTofu\nOnion\nGreen onion\nChili peppers (optional)\nDried kelp (also known as dried seaweed)\nGosari (optional)"
        print(explanation)
        print(translation)

except Exception as e:
    print(f"처리 중 오류가 발생했습니다: {e}")
