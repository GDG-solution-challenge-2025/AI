#dummy

from Food_models.food_recognition import recognize_food
import warnings
import sys
sys.stdout.reconfigure(encoding='utf-8')
warnings.filterwarnings("ignore")

# 테스트할 이미지 경로
image_path = input()
food_info=input()

try:
    # 1단계: 음식 인식 (Gemini Vision 사용)         

    food_name = "김밥"                  # dummy data

    if food_name:
        # 2단계: 음식 설명 dummy
        explanation = '''
김밥
`---___###@@@
 Kimbap
`---___###@@@





김밥은 밥과 시금치, 당근, 단무지, 계란, 그리고 햄이나 참치 등 다양한 재료를 김에 싸서 만든 음식입니다.  밥의 고소함과 다양한 재료들의 조화로 심심하면서도 맛있고, 간편하게 먹을 수 있는 맛입니다.
`---___###@@@
김밥의 정확한 유래는 명확하지 않지만, 일제강점기 시대 도시락 문화와 김에 밥을 싸 먹던 기존 한국의 식문화가 결합되어 자연스럽게 만들어진 것으로 추정됩니다.  김에 밥과 여러 재료를 싸 먹는 형태는 오래전부터 존재했으나, 현재와 같은 김밥 형태는 근대에 이르러서 완성된 것으로 보입니다.
`---___###@@@
김밥은 주로 간편한 식사 대용으로 먹습니다.  따로 밥과 함께 먹는 경우는 드물고, 김밥 자체가 밥과 여러 가지 재료가 들어있어 하나의 완성된 음식으로 취급됩니다.  국이나 다른  반찬과 함께 먹기도 하지만, 김밥만으로도 한 끼 식사가 됩니다.
`---___###@@@
밥
김
시금치
당근
단무지
어묵
계란 지단
햄
소금
참기름
소고기 (선택)
멸치 (선택)
다시마 (선택)
참깨 (선택)
`---___###@@@
없음
`---___###@@@

Kimbap is a food made by wrapping rice, spinach, carrots, pickled radish, egg, and various ingredients such as ham or tuna in seaweed.  It's a simple yet delicious taste with the fragrant rice and the harmony of various ingredients, and it's easy to eat.
`---___###@@@
The exact origin of kimbap is unclear, but it is presumed to have been naturally created through a combination of the lunchbox culture during the Japanese colonial period and the existing Korean food culture of wrapping rice in seaweed. While the practice of wrapping rice and various ingredients in seaweed has existed for a long time, the current form of kimbap seems to have been completed in the modern era.
`---___###@@@
Kimbap is mainly eaten as a convenient meal replacement. It's rare to eat it with rice separately, as kimbap itself is considered a complete meal containing rice and various ingredients.  It is sometimes eaten with soup or other side dishes, but kimbap alone constitutes a full meal.
`---___###@@@
Rice
Kim
Spinach
Carrot
Pickled radish
Fish cake
Egg omelet
Ham
Salt
Sesame oil
Beef (optional)
Dried anchovy (optional)
Kelp (optional)
Sesame (optional)
`---___###@@@
None
`---___###@@@'''
        print(explanation)

        

except FileNotFoundError:
    print(f"오류: 이미지 파일({image_path})을 찾을 수 없습니다. 경로를 확인하세요.")
except Exception as e:
    print(f"처리 중 오류가 발생했습니다: {e}")