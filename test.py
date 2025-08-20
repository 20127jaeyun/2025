import streamlit as st

# 레시피 데이터 (단계별 조리법 포함)
recipes = [
    {
        "name": "김치볶음밥",
        "main_ingredients": ["김치", "밥"],
        "ingredients": ["양파", "대파", "계란", "간장"],
        "steps": "1. 팬에 기름을 두르고 다진 양파와 대파를 볶는다.\n2. 김치를 넣고 볶는다.\n3. 밥을 넣고 간장으로 간을 한다.\n4. 계란 프라이를 올려 완성한다.",
        "difficulty": "쉬움",
        "time": 15
    },
    {
        "name": "된장찌개",
        "main_ingredients": ["된장"],
        "ingredients": ["두부", "애호박", "양파", "고추"],
        "steps": "1. 냄비에 물을 끓인다.\n2. 된장을 풀고 손질한 채소와 두부를 넣는다.\n3. 중불에서 10분간 끓인다.\n4. 마지막에 고추와 대파를 넣고 완성한다.",
        "difficulty": "보통",
        "time": 25
    },
    # ... 다른 레시피 생략 (앞서 예시처럼 계속 추가 가능) ...
]

st.title("🥘 자취생 맞춤 레시피 추천기 (적합도 표시)")

# 사용자 입력
user_input = st.text_input("가지고 있는 재료를 입력하세요 (쉼표로 구분)")
user_ingredients = [i.strip() for i in user_input.split(",") if i.strip()]

# 필터
col1, col2 = st.columns(2)
with col1:
    max_time = st.slider("최대 조리 시간 (분)", 5, 60, 60)
with col2:
    difficulty_filter = st.selectbox("난이도", ["전체", "쉬움", "보통", "어려움"])

if user_ingredients:
    scored_recipes = []

    for recipe in recipes:
        score = 0
        has_main = False

        # 메인 재료 확인
        for main in recipe["main_ingredients"]:
            if main in user_ingredients:
                score += 2
                has_main = True

        # 일반 재료 확인
        for ing in recipe["ingredients"]:
            if ing in user_ingredients:
                score += 1

        # 필터 적용
        if score > 0 and has_main:
            if recipe["time"] <= max_time:
                if difficulty_filter == "전체" or recipe["difficulty"] == difficulty_filter:
                    scored_recipes.append((score, recipe))

    # 점수순 정렬
    scored_recipes.sort(key=lambda x: x[0], reverse=True)

    if scored_recipes:
        st.subheader("추천 레시피")
        for score, recipe in scored_recipes[:10]:
            with st.expander(f"{recipe['name']} 🔥 적합도: {score}"):
                st.write(f"⏱ 조리 시간: {recipe['time']}분")
                st.write(f"📌 난이도: {recipe['difficulty']}")
                st.write(f"🥕 필요한 재료: {', '.join(recipe['main_ingredients'] + recipe['ingredients'])}")
                st.write(f"👩‍🍳 조리 방법:\n{recipe['steps']}")
    else:
        st.warning("조건에 맞는 레시피가 없습니다.")
else:
    st.info("재료를 입력하면 레시피를 추천해드려요!")
