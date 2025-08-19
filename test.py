import streamlit as st

# 다양한 레시피 데이터 (재료 + 조리법 + 난이도 + 조리시간)
def get_recipes():
    return {
        "김치볶음밥": {
            "ingredients": ["김치", "밥", "간장", "참기름"],
            "instructions": "팬에 기름을 두르고 김치를 볶다가 밥을 넣고 간장으로 간을 한 뒤 참기름을 넣어 마무리한다.",
            "difficulty": "쉬움",
            "time": 15
        },
        "계란말이": {
            "ingredients": ["계란", "소금", "당근"],
            "instructions": "계란을 풀고 소금, 다진 당근을 넣어 섞은 후 팬에 여러 번 말아가며 익힌다.",
            "difficulty": "중간",
            "time": 20
        },
        "토마토 파스타": {
            "ingredients": ["파스타면", "토마토", "올리브오일", "소금"],
            "instructions": "파스타면을 삶고, 팬에 올리브오일을 두른 후 토마토를 볶아 소스를 만든 뒤 면과 함께 버무린다.",
            "difficulty": "쉬움",
            "time": 25
        },
        "두부조림": {
            "ingredients": ["두부", "간장", "고춧가루", "파", "마늘"],
            "instructions": "두부를 썰어 팬에 올리고 간장, 고춧가루, 파, 마늘 양념을 올려 졸인다.",
            "difficulty": "쉬움",
            "time": 20
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
        # 레시피 추천 로직: 재료 일치 비율로 점수 계산
        scored_recipes = []
        for recipe, data in recipes.items():
            match_count = len(set(user_ingredients) & set(data['ingredients']))
            score = match_count / len(data['ingredients'])
            if match_count >= 1:
                scored_recipes.append((score, recipe))
        
        if scored_recipes:
            scored_recipes.sort(reverse=True)  # 점수 높은 순 정렬
            st.write("### 추천 레시피 (일치 재료 비율 기준)")
            for score, recipe in scored_recipes[:5]:  # 상위 5개 추천
                data = recipes[recipe]
                with st.expander(f"{recipe} - 난이도: {data['difficulty']}, 조리시간: {data['time']}분"):
                    st.write(f"필요 재료: {', '.join(data['ingredients'])}")
                    st.write(f"조리법: {data['instructions']}")
                    missing = set(data['ingredients']) - set(user_ingredients)
                    if missing:
                        st.info(f"❗ 추가 필요 재료: {', '.join(missing)}")
        else:
            st.warning("❌ 선택한 재료로 추천할 레시피가 없습니다.")
