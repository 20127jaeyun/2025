import streamlit as st

# 레시피 데이터 (기존 + 신규 메뉴 포함, 모두 생략 없이)
recipes = [
    # 기존 레시피
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
    # 신규 메뉴
    {
        "name": "카레라이스",
        "main_ingredients": ["밥", "카레루"],
        "ingredients": ["감자", "당근", "양파", "소고기"],
        "steps": "1. 감자, 당근, 양파, 고기를 적당히 썬다.\n2. 팬에 기름을 두르고 고기를 볶는다.\n3. 채소를 넣고 볶은 뒤 물을 부어 끓인다.\n4. 카레루를 넣고 농도를 맞춘 뒤 밥 위에 올려 완성한다.",
        "difficulty": "보통",
        "time": 40
    },
    {
        "name": "마늘버터 새우",
        "main_ingredients": ["새우"],
        "ingredients": ["마늘", "버터", "파슬리", "소금", "후추"],
        "steps": "1. 새우를 손질한다.\n2. 팬에 버터와 마늘을 볶는다.\n3. 새우를 넣고 소금, 후추로 간한다.\n4. 파슬리를 뿌려 마무리한다.",
        "difficulty": "보통",
        "time": 20
    },
    {
        "name": "부대찌개",
        "main_ingredients": ["소시지", "햄", "라면사리"],
        "ingredients": ["김치", "두부", "대파", "고추장"],
        "steps": "1. 냄비에 물을 붓고 김치를 넣는다.\n2. 소시지, 햄, 두부를 넣고 끓인다.\n3. 고추장으로 간을 맞춘 뒤 라면사리를 넣어 마무리한다.",
        "difficulty": "보통",
        "time": 30
    },
    {
        "name": "야채스프",
        "main_ingredients": ["양파", "당근"],
        "ingredients": ["감자", "브로콜리", "소금", "후추"],
        "steps": "1. 모든 채소를 먹기 좋은 크기로 썬다.\n2. 냄비에 물과 함께 끓인다.\n3. 소금, 후추로 간을 맞춘다.",
        "difficulty": "쉬움",
        "time": 20
    },
    {
        "name": "치즈라면",
        "main_ingredients": ["라면"],
        "ingredients": ["치즈", "계란", "파"],
        "steps": "1. 라면을 끓인다.\n2. 스프를 넣고 치즈를 올린다.\n3. 계란과 파를 넣고 완성한다.",
        "difficulty": "쉬움",
        "time": 10
    },
    {
        "name": "계란샐러드",
        "main_ingredients": ["계란"],
        "ingredients": ["마요네즈", "소금", "후추", "양상추"],
        "steps": "1. 계란을 삶아 으깬다.\n2. 마요네즈, 소금, 후추를 섞는다.\n3. 양상추 위에 올려 완성한다.",
        "difficulty": "쉬움",
        "time": 15
    },
    {
        "name": "참치김치전",
        "main_ingredients": ["참치캔", "김치"],
        "ingredients": ["부침가루", "물", "식용유"],
        "steps": "1. 김치와 참치를 잘게 썬다.\n2. 부침가루와 물을 섞어 반죽을 만든다.\n3. 팬에 식용유를 두르고 반죽을 부쳐 완성한다.",
        "difficulty": "보통",
        "time": 20
    },
    {
        "name": "오이무침",
        "main_ingredients": ["오이"],
        "ingredients": ["고추가루", "식초", "설탕", "소금"],
        "steps": "1. 오이를 얇게 썬다.\n2. 고추가루, 식초, 설탕, 소금으로 무친다.",
        "difficulty": "쉬움",
        "time": 10
    },
    {
        "name": "간장계란밥",
        "main_ingredients": ["밥", "계란"],
        "ingredients": ["간장", "참기름", "대파"],
        "steps": "1. 밥 위에 계란 프라이를 올린다.\n2. 간장과 참기름, 대파를 뿌려 완성한다.",
        "difficulty": "쉬움",
        "time": 5
    },
    {
        "name": "닭가슴살 샐러드",
        "main_ingredients": ["닭가슴살"],
        "ingredients": ["양상추", "방울토마토", "올리브오일", "발사믹식초"],
        "steps": "1. 닭가슴살을 구워 적당히 썬다.\n2. 양상추와 방울토마토를 섞는다.\n3. 올리브오일과 발사믹식초를 뿌려 완성한다.",
        "difficulty": "쉬움",
        "time": 20
    },
    {
        "name": "김치전",
        "main_ingredients": ["김치"],
        "ingredients": ["부침가루", "물", "식용유"],
        "steps": "1. 김치를 잘게 썬다.\n2. 부침가루와 물을 섞어 반죽을 만든다.\n3. 팬에 식용유를 두르고 반죽을 부쳐 완성한다.",
        "difficulty": "쉬움",
        "time": 15
    },
    {
        "name": "떡국",
        "main_ingredients": ["떡"],
        "ingredients": ["계란", "파", "간장", "김가루"],
        "steps": "1. 떡을 물에 넣고 끓인다.\n2. 계란을 풀어 넣고 파, 간장, 김가루로 간을 맞춘다.",
        "difficulty": "보통",
        "time": 20
    }
]

# Streamlit UI
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
        for
