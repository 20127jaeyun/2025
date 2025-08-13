import streamlit as st

# 페이지 설정
st.set_page_config(page_title="말투 분석기", page_icon="🗣️")

st.title("🗣️ 말투 분석기")
st.write("문장을 입력하면 분노, 상냥함, 유머 비율을 퍼센트로 알려드립니다.")

# 사용자 입력
user_text = st.text_area("문장을 입력하세요", placeholder="예: 안녕하세요! 오늘 기분 어때요?")

# 분석 함수
def analyze_tone(text):
    # 키워드 사전
    kindness_words = ["안녕하세요", "감사", "고맙", "잘 부탁", "좋아요", "행복", "미소", "환영"]
    anger_words = ["싫어", "짜증", "화나", "미워", "꺼져", "빡쳐", "개같", "죽어"]
    humor_words = ["ㅋㅋ", "ㅎㅎ", "재밌", "웃겨", "농담", "유머", "ㅎㅅㅎ"]

    # 점수 계산
    kindness_score = sum(text.count(w) for w in kindness_words)
    anger_score = sum(text.count(w) for w in anger_words)
    humor_score = sum(text.count(w) for w in humor_words)

    total_score = kindness_score + anger_score + humor_score

    if total_score == 0:
        return {"상냥함": 0, "분노": 0, "유머": 0}

    return {
        "상냥함": round(kindness_score / total_score * 100, 1),
        "분노": round(anger_score / total_score * 100, 1),
        "유머": round(humor_score / total_score * 100, 1)
    }

# 버튼 클릭 시 실행
if st.button("분석하기"):
    if user_text.strip() == "":
        st.warning("문장을 입력해주세요.")
    else:
        result = analyze_tone(user_text)
        st.subheader("분석 결과")
        st.write(result)

        # 시각화 (막대 그래프)
        st.bar_chart(result)
