import streamlit as st

# 레시피 데이터 (조리법 단계별 디테일)
recipes = [
    {"name": "김치볶음밥", 
     "ingredients": ["김치", "밥", "양파", "간장", "계란"], 
     "main": ["김치"], 
     "time": 15, 
     "difficulty": "쉬움", 
     "method": "1. 팬에 기름을 두르고 다진 양파와 김치를 볶는다.\n2. 밥을 넣고 함께 볶는다.\n3. 간장과 소금으로 간을 맞춘 후, 계란 프라이를 올려 완성한다."},

    {"name": "된장찌개", 
     "ingredients": ["된장", "두부", "애호박", "양파", "버섯"], 
     "main": ["된장"], 
     "time": 25, 
     "difficulty": "보통", 
     "method": "1. 냄비에 물을 끓인다.\n2. 된장을 풀고, 손질한 야채와 두부를 넣는다.\n3. 중불에서 10~15분 정도 끓인 후, 마지막에 파를 넣어 완성한다."},

    {"name": "카레라이스", 
     "ingredients": ["밥", "카레가루", "감자", "당근", "양파"], 
     "main": ["카레가루", "밥"], 
     "time": 30, 
     "difficulty": "보통", 
     "method": "1. 감자, 당근, 양파를 깍둑썰기 한다.\n2. 팬에 기름을 두르고 야채를 볶는다.\n3. 카레가루와 물을 넣고 끓인다.\n4. 밥 위에 카레를 부어 완성한다."},

    {"name": "불고기", 
     "ingredients": ["소고기", "간장", "설탕", "양파", "파"], 
     "main": ["소고기"], 
     "time": 35, 
     "difficulty": "보통", 
     "method": "1. 소고기를 얇게 썰어 간장, 설탕, 다진 마늘, 파와 함께 재운다.\n2. 팬에 볶아 익힌 후 접시에 담아 완성한다."},

    {"name": "김밥", 
     "ingredients": ["밥", "김", "계란", "시금치", "단무지"], 
     "main": ["밥", "김"], 
     "time": 40, 
     "difficulty": "어려움", 
     "method": "1. 재료를 준비하고, 계란은 지단으로 부친다.\n2. 김 위에 밥을 펼치고 재료를 올린다.\n3. 김밥을 단단히 말아 먹기 좋게 썬다."},

    {"name": "토마토 파스타", 
     "ingredients": ["파스타", "토마토", "양파", "마늘"], 
     "main": ["파스타", "토마토"], 
     "time": 30, 
     "difficulty": "보통", 
     "method": "1. 파스타를 삶는다.\n2. 팬에 기름을 두르고 다진 마늘과 양파를 볶는다.\n3. 토마토를 넣고 소스를 만들고, 파스타와 섞어 완성한다."},

    {"name": "참치마요덮밥", 
     "ingredients": ["참치캔", "마요네즈", "밥", "간장"], 
     "main": ["참치캔", "밥"], 
     "time": 10, 
     "difficulty": "쉬움", 
     "method": "1. 참치캔의 물기를 제거한다.\n2. 마요네즈와 간장 1작은술을 넣고 섞는다.\n3. 밥 위에 올리고 잘 섞어서 먹는다."},

    {"name": "떡볶이", 
     "ingredients": ["떡", "고추장", "어묵", "파"], 
     "main": ["떡", "고추장"], 
     "time": 20, 
     "difficulty": "보통", 
     "method": "1. 떡과 어묵을 준비한다.\n2. 고추장, 물, 설탕을 섞어 소스를 만든다.\n3. 떡과 어묵을 넣고 졸이듯 볶아 완성한다."},

    {"name": "감자볶음", 
     "ingredients": ["감자", "간장", "기름", "소금"], 
     "main": ["감자"], 
     "time": 15, 
     "difficulty": "쉬움", 
     "method": "1. 감자를 얇게 채썬다.\n2. 팬에 기름을 두르고 감자를 볶는다.\n3. 소금과 간장으로 간을 맞춘 후 완성한다."},

    {"name": "스팸구이", 
     "ingredients": ["스팸", "간장", "마늘"], 
     "main": ["스팸"], 
     "time": 10, 
     "difficulty": "쉬움", 
     "method": "1. 스팸을 먹기 좋게 썬다.\n2. 팬에 구워 간장과 다진 마늘을 발라가며 익힌다."},

    {"name": "토스트", 
     "ingredients": ["식빵", "계란", "버터", "치즈"], 
     "main": ["식빵", "계란"], 
     "time": 10, 
     "difficulty": "쉬움", 
     "method": "1. 식빵 위에 계란을 올리고 팬에 굽는다.\n2. 치즈를 올려 녹이면 완성한다."}
]

# 제목
st.title("🍳 자취생 맞춤 레시피 추천기 (단계별 조리법)")

# 사용자 입력
user_input = st.text_input("냉장고에 있는 재료를 입력하세요 (쉼표로 구분):", "")
user_ingredients = [i.strip() for i in user_input.split(",") if i.strip()]

# 추천 로직
if user_ingredients:
    results = []
    for recipe in recipes:
        score = 0
        matched_main = [m for m in recipe["main"] if m in user_ingredients]
        matched_ingredients = [i for i in recipe["ingredients"] if i in user_ingredients]

        if matched_main:
            score += 2 * len(matched_main)
        score += len(matched_ingredients)

        if score > 0 and matched_main:  # 메인 재료 반드시 포함
            results.append((recipe, score))

    results.sort(key=lambda x: x[1], reverse=True)

    if results:
        st.subheader("✨ 추천 레시피 ✨")
        for recipe, score in results:
            st.markdown(f"### 🍽 {recipe['name']}")
            st.write(f"⏱ 소요 시간: **{recipe['time']}분**")
            st.write(f"📌 난이도: **{recipe['difficulty']}**")
            st.write(f"🥕 필요 재료: {', '.join(recipe['ingredients'])}")
            st.write(f"👨‍🍳 조리법:\n{recipe['method']}")
            st.write("---")
    else:
        st.error("조건에 맞는 레시피가 없습니다.")
