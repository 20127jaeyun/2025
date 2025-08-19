import streamlit as st

# 다양한 레시피 데이터 (재료 + 조리법)
def get_recipes():
    return {
        "김치볶음밥": {
            "ingredients": ["김치", "밥", "간장", "참기름"],
            "instructions": "팬에 기름을 두르고 김치를 볶다가 밥을 넣고 간장으로 간을 한 뒤 참기름을 넣어 마무리한다."
        },
        "계란말이": {
            "ingredients": ["계란", "소금", "당근"],
            "instructions": "계란을 풀고 소금, 다진 당근을 넣어 섞은 후 팬에 여러 번 말아가며 익힌다."
        },
        "토마토 파스타": {
            "ingredients": ["파스타면", "토마토", "올리브오일", "소금"],
            "instructions": "파스타면을 삶고, 팬에 올리브오일을 두른 후 토마토를 볶아 소스를 만든 뒤 면과 함께 버무린다."
        },
        "된장찌개": {
            "ingredients": ["된장", "두부", "애호박", "양파"],
            "instructions": "냄비에 물을 붓고 된장을 풀어 끓인 뒤 두부, 애호박, 양파를 넣고 끓인다."
        },
        "샐러드": {
            "ingredients": ["상추", "오이", "토마토", "드레싱"],
            "instructions": "야채를 먹기 좋은 크기로 썰고 그릇에 담은 뒤 드레싱을 뿌려 섞는다."
        }
        # ... 더 많은 레시피 생략 ...
    }

recipes = get_recipes()

st.title("🥘 냉장고 속 재료로 레시피 추천하기")

# 사용자 입력
ingredients = st.text_input("냉장고 속 재료를 입력하세요 (쉼표로 구분)")  # 기본값 제거
user_ingredients = [i.strip() for i in ingredients.split(',')]

if st.button("레시피 추천받기"):
    st.write("### 사용 가능한 레시피:")
    found = False
    for recipe, data in recipes.items():
        req_ingredients = data["ingredients"]
        instructions = data["instructions"]
        
        # 입력한 재료 중 1개 이상 포함되면 추천
        match_count = len(set(user_ingredients) & set(req_ingredients))
        if match_count >= 1:
            st.success(f"✅ {recipe}")
            st.write(f"필요 재료: {', '.join(req_ingredients)}")
            st.write(f"조리법: {instructions}")
            found = True
    
    if not found:
        st.warning("❌ 해당 재료로는 추천할 레시피가 없어요.")
