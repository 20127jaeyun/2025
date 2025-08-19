import streamlit as st

# 다양한 레시피 데이터 (메인 재료 리스트 + 재료 + 조리법 + 난이도 + 조리시간)
def get_recipes():
    return {
        "김치볶음밥": {
            "main_ingredients": ["김치"],
            "ingredients": ["김치", "밥", "간장", "참기름"],
            "instructions": "팬에 기름을 두르고 김치를 볶다가 밥을 넣고 간장으로 간을 한 뒤 참기름을 넣어 마무리한다.",
            "difficulty": "쉬움",
            "time": 15
        },
        "계란말이": {
            "main_ingredients": ["계란"],
            "ingredients": ["계란", "소금", "당근", "양파"],
            "instructions": "계란을 풀고 소금, 다진 당근, 양파를 넣어 섞은 후 팬에 여러 번 말아가며 익힌다.",
            "difficulty": "중간",
            "time": 20
        },
        "토마토 파스타": {
            "main_ingredients": ["파스타면", "토마토"],
            "ingredients": ["파스타면", "토마토", "올리브오일", "소금", "마늘", "바질"],
            "instructions": "파스타면을 삶고, 팬에 올리브오일을 두른 후 토마토와 마늘을 볶아 소스를 만든 뒤 면과 함께 버무리고 바질을 올린다.",
            "difficulty": "쉬움",
            "time": 25
        },
        "두부조림": {
            "main_ingredients": ["두부"],
            "ingredients": ["두부", "간장", "고춧가루", "파", "마늘", "설탕"],
            "instructions": "두부를 썰어 팬에 올리고 간장, 고춧가루, 파, 마늘, 설탕 양념을 올려 졸인다.",
            "difficulty": "쉬움",
            "time": 20
        },
        "된장찌개": {
            "main_ingredients": ["된장"],
            "ingredients": ["된장", "두부", "애호박", "양파", "대파", "버섯"],
            "instructions": "냄비에 물을 붓고 된장을 풀어 끓인 뒤 두부, 애호박, 양파, 대파, 버섯을 넣고 끓인다.",
            "difficulty": "중간",
            "time": 30
        },
        "김밥": {
            "main_ingredients": ["김", "밥"],
            "ingredients": ["김", "밥", "당근", "단무지", "계란", "시금치", "햄"],
            "instructions": "밥과 속재료를 김 위에 올리고 돌돌 말아 썰어서 완성한다.",
            "difficulty": "중간",
            "time": 25
        },
        "감자조림": {
            "main_ingredients": ["감자"],
            "ingredients": ["감자", "간장", "설탕", "참기름", "마늘", "파"],
            "instructions": "감자를 먹기 좋은 크기로 썰고 간장, 설탕, 참기름, 마늘, 파로 졸인다.",
            "difficulty": "쉬움",
            "time": 25
        },
        "계란국": {
            "main_ingredients": ["계란"],
            "ingredients": ["계란", "파", "소금", "물"],
            "instructions": "물에 소금을 넣고 끓인 후 계란을 풀고 파를 넣어 마무리한다.",
            "difficulty": "쉬움",
            "time": 10
        },
        "잡채": {
            "main_ingredients": ["당면"],
            "ingredients": ["당면", "소고기", "시금치", "당근", "양파", "간장", "참기름"],
            "instructions": "당면을 삶아두고 소고기와 채소를 볶아 간장으로 간한 뒤 섞어준다.",
            "difficulty": "중간",
            "time": 35
        }
    }

recipes = get_recipes()

st.title("🥘 냉장고 속 재료로 레시피 추천하기")

# 사용자 입력 (직접 입력)
ingredients_input = st.text_input("냉장고 속 재료를 입력하세요 (쉼표로 구분)")
user_ingredients = [i.strip() for i in ingredients_input.split(',') if i.strip()]

if st.button("레시피 추천받기"):
    if not user_ingredients:
        st.warning("❌ 재료를 입력해주세요.")
    else:
        # 레시피 추천 로직: 메인 재료 중 하나라도 있어야 추천
        scored_recipes = []
        for recipe, data in recipes.items():
            if any(main in user_ingredients for main in data['main_ingredients']):
                match_count = len(set(user_ingredients) & set(data['ingredients']))
                score = match_count / len(data['ingredients'])
                scored_recipes.append((score, recipe))
        
        if scored_recipes:
            scored_recipes.sort(reverse=True)  # 점수 높은 순 정렬
            st.write("### 추천 레시피 (메인 재료 포함, 일치 재료 비율 기준)")
            for score, recipe in scored_recipes[:5]:  # 상위 5개 추천
                data = recipes[recipe]
                with st.expander(f"{recipe} - 난이도: {data['difficulty']}, 조리시간: {data['time']}분"):
                    st.write(f"필요 재료: {', '.join(data['ingredients'])}")
                    st.write(f"조리법: {data['instructions']}")
                    missing = set(data['ingredients']) - set(user_ingredients)
                    if missing:
                        st.info(f"❗ 추가 필요 재료: {', '.join(missing)}")
        else:
            st.warning("❌ 선택한 재료에 레시피의 메인 재료가 포함되지 않아 추천할 레시피가 없습니다.")
