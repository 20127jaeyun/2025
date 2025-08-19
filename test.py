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
        },
        "불고기": {
            "ingredients": ["소고기", "간장", "설탕", "양파", "마늘"],
            "instructions": "소고기를 간장, 설탕, 마늘, 양파와 함께 재운 후 팬에 볶아 익힌다."
        },
        "카레라이스": {
            "ingredients": ["카레가루", "감자", "당근", "양파", "밥"],
            "instructions": "냄비에 감자, 당근, 양파를 볶다가 물을 넣고 끓인 뒤 카레가루를 풀어 밥 위에 얹는다."
        },
        "김치찌개": {
            "ingredients": ["김치", "돼지고기", "두부", "양파", "대파"],
            "instructions": "냄비에 돼지고기를 볶다가 김치를 넣고 물을 부어 끓인 뒤 두부와 대파를 넣는다."
        },
        "라면": {
            "ingredients": ["라면", "물", "계란", "파"],
            "instructions": "끓는 물에 라면과 스프를 넣고 끓이다가 계란과 파를 넣어 완성한다."
        },
        "비빔국수": {
            "ingredients": ["소면", "고추장", "오이", "계란", "김치"],
            "instructions": "소면을 삶아 찬물에 헹군 뒤 고추장 양념과 함께 비비고 오이, 계란, 김치를 곁들인다."
        },
        "떡볶이": {
            "ingredients": ["떡", "고추장", "어묵", "대파"],
            "instructions": "떡과 어묵을 물에 넣고 끓이다가 고추장과 대파를 넣어 양념이 배도록 끓인다."
        },
        "오므라이스": {
            "ingredients": ["밥", "계란", "케찹", "양파", "당근"],
            "instructions": "밥을 양파, 당근과 함께 볶아 케찹으로 간한 뒤 계란 지단으로 덮는다."
        },
        "피자": {
            "ingredients": ["피자도우", "치즈", "토마토소스", "양파", "피망"],
            "instructions": "피자도우 위에 토마토소스를 바르고 치즈, 양파, 피망을 올린 뒤 오븐에 구운다."
        },
        "잡채": {
            "ingredients": ["당면", "소고기", "시금치", "당근", "양파", "간장"],
            "instructions": "당면을 삶아두고 소고기와 채소를 볶아 간장으로 간한 뒤 섞어준다."
        },
        "갈비찜": {
            "ingredients": ["소갈비", "간장", "배", "대파", "마늘"],
            "instructions": "소갈비를 간장, 배, 대파, 마늘 양념에 재운 후 냄비에 넣고 푹 찐다."
        }
    }

recipes = get_recipes()

st.title("🥘 냉장고 속 재료로 레시피 추천하기")

# 사용자 입력
ingredients = st.text_input("냉장고 속 재료를 입력하세요 (쉼표로 구분)", "김치, 밥, 계란")
user_ingredients = [i.strip() for i in ingredients.split(',')]

if st.button("레시피 추천받기"):
    st.write("### 사용 가능한 레시피:")
    found = False
    for recipe, data in recipes.items():
        req_ingredients = data["ingredients"]
        instructions = data["instructions"]
        
        # 입력 재료 중 최소 2개 이상 포함되면 추천
        match_count = len(set(user_ingredients) & set(req_ingredients))
        if match_count >= 2:
            st.success(f"✅ {recipe}")
            st.write(f"필요 재료: {', '.join(req_ingredients)}")
            st.write(f"조리법: {instructions}")
            found = True
    
    if not found:
        st.warning("❌ 해당 재료로는 추천할 레시피가 없어요.")

