import streamlit as st

# 레시피 데이터 (완전판, 단계별 조리법)
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
    {
        "name": "김밥",
        "main_ingredients": ["김", "밥"],
        "ingredients": ["계란", "시금치", "단무지", "햄"],
        "steps": "1. 계란 지단을 부친다.\n2. 김 위에 밥을 펼치고 재료를 올린다.\n3. 단단히 말아서 먹기 좋게 썬다.",
        "difficulty": "보통",
        "time": 40
    },
    {
        "name": "토마토 파스타",
        "main_ingredients": ["토마토", "파스타"],
        "ingredients": ["올리브오일", "마늘", "양파", "치즈"],
        "steps": "1. 파스타를 삶는다.\n2. 팬에 올리브오일을 두르고 마늘과 양파를 볶는다.\n3. 토마토를 넣어 소스를 만든다.\n4. 파스타와 섞고 치즈를 올려 완성한다.",
        "difficulty": "보통",
        "time": 30
    },
    {
        "name": "두부조림",
        "main_ingredients": ["두부"],
        "ingredients": ["간장", "마늘", "파", "고춧가루"],
        "steps": "1. 두부를 먹기 좋은 크기로 자른다.\n2. 팬에 두부를 올리고 앞뒤로 살짝 굽는다.\n3. 간장, 마늘, 파, 고춧가루로 양념장을 만든 뒤 졸인다.",
        "difficulty": "쉬움",
        "time": 20
    },
    {
        "name": "참치마요덮밥",
        "main_ingredients": ["참치캔", "밥"],
        "ingredients": ["마요네즈", "간장"],
        "steps": "1. 참치캔 물기를 제거한다.\n2. 마요네즈와 간장을 넣고 섞는다.\n3. 밥 위에 올리고 섞어 먹는다.",
        "difficulty": "쉬움",
        "time": 10
    },
    {
        "name": "떡볶이",
        "main_ingredients": ["떡", "고추장"],
        "ingredients": ["어묵", "파", "설탕"],
        "steps": "1. 떡과 어묵을 준비한다.\n2. 고추장, 설탕, 물로 소스를 만든다.\n3. 떡과 어묵을 넣고 졸이듯 볶아 완성한다.",
        "difficulty": "보통",
        "time": 20
    },
    {
        "name": "계란말이",
        "main_ingredients": ["계란"],
        "ingredients": ["파", "소금"],
        "steps": "1. 계란을 풀어 소금과 다진 파를 섞는다.\n2. 팬에 부쳐 여러 번 말아 완성한다.",
        "difficulty": "쉬움",
        "time": 10
    },
    {
        "name": "오므라이스",
        "main_ingredients": ["밥", "계란"],
        "ingredients": ["케첩", "양파", "당근"],
        "steps": "1. 양파와 당근을 볶는다.\n2. 밥을 넣고 케첩과 함께 볶는다.\n3. 계란으로 밥을 감싸 완성한다.",
        "difficulty": "보통",
        "time": 20
    },
    {
        "name": "스팸구이",
        "main_ingredients": ["스팸"],
        "ingredients": ["간장", "마늘"],
        "steps": "1. 스팸을 먹기 좋은 크기로 자른다.\n2. 팬에 굽고, 간장과 다진 마늘을 바르며 익힌다.",
        "difficulty": "쉬움",
        "time": 10
    },
    {
        "name": "토스트",
        "main_ingredients": ["식빵", "계란"],
        "ingredients": ["버터", "치즈", "햄"],
        "steps": "1. 팬에 버터를 녹이고 식빵을 굽는다.\n2. 계란, 치즈, 햄을 올려 완성한다.",
        "difficulty": "쉬움",
        "time": 10
    },
    {
        "name": "감자볶음",
        "main_ingredients": ["감자"],
        "ingredients": ["간장", "소금", "기름"],
        "steps": "1. 감자를 얇게 채썬다.\n2. 팬에 기름을 두르고 볶는다.\n3. 간장과 소금으로 간을 맞춘다.",
        "difficulty": "쉬움",
        "time": 15
    },
    {
        "name": "크림 파스타",
        "main_ingredients": ["파스타"],
        "ingredients": ["생크림", "베이컨", "양파", "버터"],
        "steps": "1. 파스타를 삶는다.\n2. 팬에 버터를 녹이고 베이컨과 양파를 볶는다.\n3. 생크림을 넣고 소스를 만든 뒤 파스타와 섞는다.",
        "difficulty": "보통",
        "time": 30
    }
]

st.title("🥘 자취생 맞춤 레시피 추천기 (완전판, 상세 조리법)")

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
            with st.expander(f"{recipe['name']} (점수: {score})"):
                st.write(f"⏱ 조리 시간: {recipe['time']}분")
                st.write(f"📌 난이도: {recipe['difficulty']}")
                st.write(f"🥕 필요한 재료: {', '.join(recipe['main_ingredients'] + recipe['ingredients'])}")
                st.write(f"👩‍🍳 조리 방법:\n{recipe['steps']}")
    else:
        st.warning("조건에 맞는 레시피가 없습니다.")
else:
    st.info("재료를 입력하면 레시피를 추천해드려요!")
