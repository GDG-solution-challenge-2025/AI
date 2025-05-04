#dummy

from Food_models.food_recognition import recognize_food
from Food_models.food_explanation_gemma import explain_food_gemma # Gemma 버전 함수 임포트
from Food_models.gemma_translation import trans_eng
import warnings
warnings.filterwarnings("ignore")

# 테스트할 이미지 경로
image_path = input("파일 경로: ")
food_info=input('못먹는 음식 정보: ')

try:
    # 1단계: 음식 인식 (Gemini Vision 사용)         

    food_name = "김치찌개"                  # dummy data

    if food_name:
        # 2단계: 음식 설명 dummy
        explanation = '''숯불소갈비는 달콤하고 짭짤한 맛이 조화롭게 어우러져 밥반찬으로도 좋고, 술안주로도 훌륭한 음식입니다. 숯불에 구워내어 풍미가 깊어지는 소갈비
는 남녀노소 누구나 좋아하는 맛을 선호하는 메뉴입니다.
`---___###@@@
숯불소갈비는 조선시대 궁중에서 유행했던 음식으로, 숯불에 구워 먹는 소갈비는 당시 귀족들의 고급 음식이었으며, 숯불의 향연을 연상시키는 풍미가 특징입니다. 이후 한국전통 음식으로 자리 잡으면서, 지역별로 다양한 방식으로 발전하여 오늘날의 대표적인 음식으로 자리 잡았습니다.
`---___###@@@
숯불소갈비는 숯불에 구워 먹는 대표적인 음식으로, 얇게 썬 소갈비를 숯불에 구워 겉은 바삭하고 속은 촉촉하게 즐길 수 있습니다. 쌈 채소, 쌈장,  쌈김치 등과 함께 곁들여 먹으면 더욱 맛있습니다.
`---___###@@@
*   소고기 (다리살, 목살, 등심 등)
*   양파
*   대파
*   마늘
*   청양고추
*   물
*   설탕
*   소금
*   후추
*   참기름
*   식용유
`---___###@@@'''
        translation = '''Grilled barbecue ribs have a sweet and savory flavor that blends harmoniously, making them a great side dish for rice and also a wonderful appetizer for drinks. The flavorful ribs, cooked over an open flame, develop a rich taste when grilled. This dish is a favorite among both men and women, appealing to everyone who enjoys a taste that is universally liked.
`---___###@@@
Charcoal-grilled ribs were a popular dish in the Joseon Dynasty, a luxury food enjoyed by the aristocracy and characterized by the aroma of a bonfire. As it became a traditional Korean dish, it evolved regionally and is now a representative food in Korea today.
`---___###@@@
Grilled ribs are a popular dish that is grilled and enjoyed by eating thinly sliced beef. They are crispy on the outside and juicy on the inside. They are often served with kimchi and kimchi dip and are more delicious when paired with it.
`---___###@@@
Beef (ribs, sirloin, heart)
onions, scallions
garlic
chili peppers
water
sugar
salt
pepper
sesame oil
cooking oil
`---___###@@@'''
        print(explanation)
        print(translation)

        

except FileNotFoundError:
    print(f"오류: 이미지 파일({image_path})을 찾을 수 없습니다. 경로를 확인하세요.")
except Exception as e:
    print(f"처리 중 오류가 발생했습니다: {e}")