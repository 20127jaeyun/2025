import streamlit as st

# 레시피 데이터
recipes = [
    {
        "name": "김치볶음밥",
        "ingredients": ["김치", "밥", "양파", "간장", "계란"],
        "main": ["김치"],
        "time": 15,
        "difficulty": "쉬움"
    },
    {
        "name": "된장찌개",
        "ingredients": ["된장", "두부", "애호박", "양파", "버섯"],
        "main": ["된장"],
        "time": 25,
        "difficulty": "보통"
    },
    {
        "name": "카레라이스",
        "ingredients": ["밥", "카레가루", "감자", "당근", "양파"],
        "main": ["카레가루", "밥"],
        "time": 30,
        "difficulty": "보통"
    },
    {
        "name": "불고기",
        "ingredients": ["소고기", "간장", "설탕", "양파", "파"],
        "main": ["소고기"],
        "time": 35,
        "difficulty": "보통"
    },
    {
        "name": "김밥",
        "ingredients": ["밥", "김", "계란", "시금치", "단무지"],
        "main": ["밥", "김"],
        "time": 40,
        "difficulty": "어려움"
    },
    {
        "name": "토마토 파스타",
        "ingredients": ["파스타", "토마토", "양파", "마늘"],
        "main": ["파스타", "토마토"],
        "time": 30,
        "difficulty": "보통"
    },
    {
        "name": "크림 파스타",
        "ingredients": ["파스타", "생크림", "양파", "베이컨"],
        "main": ["파스타"],
        "time": 30,
        "difficulty": "보통"
    },
    {
        "name": "계란말이",
        "ingredients": ["계란", "파", "소금"],
        "main": ["계란"],
        "time": 10,
        "difficulty": "쉬움"
    },
    {
        "name": "오므라이스",
        "ingredients": ["밥", "계란", "케첩", "양파"],
        "main": ["밥", "계란"],
        "time": 20,
        "difficulty": "보통"
    },
    {
        "name": "두부조림",
        "ingredients": ["두부", "간장", "마늘", "파"],
        "main": ["두부"],
        "time": 20,
        "difficulty": "쉬움"
    },
    {
        "name": "된장국",
        "ingredients": ["된장", "두부", "파", "애호박"],
        "main": ["된장"],
        "time": 20,
        "difficulty": "쉬움"
    },
    {
        "name": "김치찌개",
        "ingredients": ["김치", "두부", "돼지고기", "파"],
        "main": ["김치"],
        "time": 35,
        "difficulty": "보통"
    },
    {
        "name": "부침개 (김치전)",
        "ingredients": ["김치", "부침가루", "계란"],
        "main": ["김치"],
        "time": 25,
        "difficulty": "쉬움"
    },
    {
        "name": "샐러드",
        "ingredients": ["양상추", "토마토", "오이", "드레싱"],
        "main": ["양상추"],
        "time": 10,
        "difficulty": "쉬움"
    },
    {
        "name": "치킨",
        "ingredients": ["닭고기", "간장", "마늘", "양파"],
        "main": ["닭고기"],
        "time": 60,
        "difficulty": "어려움"
    },
    {
        "name": "갈비찜",
        "ingredients": ["소갈비", "무", "간장", "마늘", "대파"],
        "main": ["소갈비"],
        "time": 90,
        "difficulty": "어려움"
    },
]

# 제목
st.title("🍳 레시피 추천 앱")

# 사용자 입력
user_input = st.text_input("재료를 입력하세요 (쉼표로 구분):", "")
user_ingredients = [i.strip() for i in user_input.split(",") if i.strip()]

# 추천 로직
if user_ingredients:
    results = []
    for recipe in recipes:
        score = 0
        matched_main = [m for m in recipe["main"] if m in user_ingredients]
        matched_ingredients = [i for i in recipe["ingredients"] if i in user_ingredients]

        if matched_main:
            score += 2 * len(matched_main)  # 메인 재료 가산점
        score += len(matched_ingredients)

        if score > 0 and matched_main:  # 반드시 메인재료 포함해야 추천
            results.append((recipe, score))

    results.sort(key=lambda x: x[1], reverse=True)

    if results:
        st.subheader("🍴 추천 레시피")
        for recipe, score in results:
            st.write(f"**{recipe['name']}**")
            st.write(f"- 필요 재료: {', '.join(recipe['ingredients'])}")
            st.write(f"- 조리 시간: {recipe['time']}분")
            st.write(f"- 난이도: {recipe['difficulty']}")
            st.write("---")
    else:
        st.write("조건에 맞는 레시피가 없습니다.")
