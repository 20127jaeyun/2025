import streamlit as st

# =========================
# 레시피 데이터 (메인재료, 일반재료, 난이도, 시간, 조리법)
# =========================
recipes = [
    {
        "name": "김치볶음밥",
        "main_ingredients": ["김치", "밥"],
        "ingredients": ["양파", "대파", "계란", "간장"],
        "steps": "1. 팬에 기름을 두르고 다진 양파와 대파를 볶는다.\n"
                 "2. 김치를 넣고 볶는다.\n"
                 "3. 밥을 넣고 간장으로 간을 한다.\n"
                 "4. 계란 프라이를 올려 완성한다.",
        "difficulty": "쉬움",
        "time": 15
    },
    {
        "name": "된장찌개",
        "main_ingredients": ["된장"],
        "ingredients": ["두부", "애호박", "양파", "고추"],
        "steps": "1. 냄비에 물을 끓인다.\n"
                 "2. 된장을 풀고 손질한 채소와 두부를 넣는다.\n"
                 "3. 중불에서 10분간 끓인다.\n"
                 "4. 마지막에 고추와 대파를 넣고 완성한다.",
        "difficulty": "보통",
        "time": 25
    },
    {
        "name": "김밥",
        "main_ingredients": ["김", "밥"],
        "ingredients": ["계란", "시금치", "단무지", "햄"],
        "steps": "1. 계란 지단을 부친다.\n"
                 "2. 김 위에 밥을 펼치고 재료를 올린다.\n"
                 "3. 단단히 말아서 먹기 좋게 썬다.",
        "difficulty": "보통",
        "time": 40
    },
    {
        "name": "토마토 파스타",
        "main_ingredients": ["토마토", "파스타"],
        "ingredients": ["올리브오일", "마늘", "양파", "치즈"],
        "steps": "1. 파스타를 삶는다.\n"
                 "2. 팬에 올리브오일을 두르고 마늘과 양파를 볶는다.\n"
                 "3. 토마토를 넣어 소스를 만든다.\n"
                 "4. 파스타와 섞고 치즈를 올려 완성한다.",
        "difficulty": "보통",
        "time": 30
    },
    {
        "name": "두부조림",
        "main_ingredients": ["두부"],
        "ingredients": ["간장", "마늘", "파", "고춧가루"],
        "steps": "1. 두부를 먹기 좋은 크기로 자른다.\n"
                 "2. 팬에 두부를 올리고 앞뒤로 살짝 굽는다.\n"
                 "3. 간장, 마늘, 파, 고춧가루로 양념장을 만든 뒤 졸인다.",
        "difficulty": "쉬움",
        "time": 20
    },
    {
        "name": "참치마요덮밥",
        "main_ingredients": ["참치캔", "밥"],
        "ingredients": ["마요네즈", "간장"],
        "steps": "1. 참치캔 물기를 제거한다.\n"
                 "2. 마요네즈와 간장을 넣고 섞는다.\n"
                 "3. 밥 위에 올리고 섞어 먹는다.",
        "difficulty": "쉬움",
        "time": 10
    },
    {
        "name": "떡볶이",
        "main_ingredients": ["떡", "고추장"],
        "ingredients": ["어묵", "파", "설탕"],
        "steps": "1. 떡과 어묵을 준비한다.\n"
                 "2. 고추장, 설탕, 물로 소스를 만든다.\n"
                 "3. 떡과 어묵을 넣고 졸이듯 볶아 완성한다.",
        "difficulty": "보통",
        "time": 20
    },
    {
        "name": "계란말이",
        "main_ingredients": ["계란"],
        "ingredients": ["파", "소금"],
        "steps": "1. 계란을 풀어 소금과 다진 파를 섞는다.\n"
                 "2. 팬에 부쳐 여러 번 말아 완성한다.",
        "difficulty": "쉬움",
        "time": 10
    },
    {
        "name": "오므라이스",
        "main_ingredients": ["밥", "계란"],
        "ingredients": ["케첩", "양파", "당근"],
        "steps": "1. 양파와 당근을 볶는다.\n"
                 "2. 밥을 넣고 케첩과 함께 볶는다.\n"
                 "3. 계란으로 밥을 감싸 완성한다.",
        "difficulty": "보통",
        "time": 20
    },
    {
        "name": "스팸구이",
        "main_ingredients": ["스팸"],
        "ingredients": ["간장", "마늘"],
        "steps": "1. 스팸을 먹기 좋은 크기로 자른다.\n"
                 "2. 팬에 굽고, 간장과 다진 마늘을 바르며 익힌다.",
        "difficulty": "쉬움",
        "time": 10
    },
    {
        "name": "카레라이스",
        "main_ingredients": ["밥", "카레루"],
        "ingredients": ["감자", "당근", "양파", "소고기"],
        "steps": "1. 감자, 당근, 양파, 고기를 적당히 썬다.\n"
                 "2. 팬에 기름을 두르고 고기를 볶는다.\n"
                 "3. 채소를 넣고 볶은 뒤 물을 부어 끓인다.\n"
                 "4. 카레루를 넣고 농도를 맞춘 뒤 밥 위에 올려 완성한다.",
        "difficulty": "보통",
        "time": 40
    },
    {
        "name": "마늘버터 새우",
        "main_ingredients": ["새우"],
        "ingredients": ["마늘", "버터", "파슬리", "소금", "후추"],
        "steps": "1. 새우를 손질한다.\n"
                 "2. 팬에 버터와 마늘을 볶는다.\n"
                 "3. 새우를 넣고 소금, 후추로 간한다.\n"
                 "4. 파슬리를 뿌려 마무리한다.",
        "difficulty": "보통",
        "time": 20
    }
    # 필요하면 여기서 추가 메뉴 계속 넣을 수 있음
]

# =========================
# Streamlit UI
# =========================
st.title("🥘 자취생 맞춤 레시피 추천기 (🔥 적합도 표시)")

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
        main_match_count = 0

        # 메인 재료 확인
        for main in recipe["main_ingredients"]:
            if main in user_ingredients:
                main_match_count += 1

        # 메인재료 1개만 있으면 적합도 1
        if main_match_count == 1:
            score += 1
        elif main_match_count > 1:
            score += 2 * main_match_count

        # 일반 재료 확인
        for ing in recipe["ingredients"]:
            if ing in user_ingredients:
                score += 1

        # 메인재료 없으면 추천 안함
        if main_match_count >= 1:
            # 필터 적용
            if recipe["time"] <= max_time:
                if difficulty_filter == "전체" or recipe["difficulty"] == difficulty_filter:
                    scored_recipes.append((score, recipe))

    # 점수순 정렬
    scored_recipes.sort(key=lambda x: x[0], reverse=True)

    if scored_recipes:
        st.subheader("추천 레시피")
        for score, recipe in scored_recipes:
            with st.expander(f"{recipe['name']} 🔥 적합도: {score}"):
                st.write(f"⏱ 조리 시간: {recipe['time']}분")
                st.write(f"📌 난이도: {recipe['difficulty']}")
                st.write(f"🥕 필요한 재료: {', '.join(recipe['main_ingredients'] + recipe['ingredients'])}")
                st.write(f"👩‍🍳 조리 방법:\n{recipe['steps']}")
    else:
        st.warning("조건에 맞는 레시피가 없습니다.")
else:
    st.info("재료를 입력하면 레시피를 추천해드려요!")
