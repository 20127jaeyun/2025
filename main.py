import streamlit as st
import openai
import json
from PIL import Image
import base64

# ——— OpenAI API 키 설정 ———
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ——— 페이지 설정 ———
st.set_page_config(
    page_title="✨ 화려한 AI 말투 분석기 ✨",
    page_icon="🗣️",
    layout="wide"
)

# ——— 배경 그라데이션 CSS ———
page_bg_img = """
<style>
body {
    background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
    color: #111;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
section.main > div.block-container {
    padding: 2rem 3rem 4rem 3rem;
    background: rgba(255, 255, 255, 0.85);
    border-radius: 20px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.2);
}
h1 {
    font-weight: 900 !important;
    font-size: 3.5rem !important;
    text-align: center;
    color: #3b0a45;
    text-shadow: 2px 2px 6px #ffd6f7;
    margin-bottom: 0.1rem !important;
}
h3 {
    font-weight: 700 !important;
    color: #6a097d;
    text-align: center;
}
button[kind="primary"] {
    background: linear-gradient(90deg, #f72585 0%, #b5179e 100%) !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 1.25rem !important;
    padding: 0.6rem 2rem !important;
    border-radius: 15px !important;
    box-shadow: 0 8px 20px rgba(245, 37, 133, 0.6) !important;
    transition: 0.3s;
}
button[kind="primary"]:hover {
    background: linear-gradient(90deg, #b5179e 0%, #f72585 100%) !important;
    box-shadow: 0 12px 35px rgba(181, 23, 158, 0.8) !important;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# ——— 타이틀과 부제 ———
st.markdown("<h1>✨ 화려한 AI 말투 분석기 🗣️</h1>", unsafe_allow_html=True)
st.markdown("<h3>문장을 입력하면 GPT가 분노😡, 상냥함😇, 유머😂 비율을 세밀하게 분석해줍니다!</h3>", unsafe_allow_html=True)
st.markdown("---")

# ——— 입력 박스 ———
user_text = st.text_area(
    "분석할 문장을 입력해주세요 ✍️",
    height=180,
    max_chars=1000,
    placeholder="예) 오늘 너무 피곤하지만, 너랑 얘기하니까 기분 좋아 ㅎㅎ"
)

# ——— AI 분석 함수 ———
def analyze_tone_ai(text):
    prompt = f"""
다음 문장의 말투를 분석해서 분노, 상냥함, 유머의 비율(%)을 JSON 형식으로 반환해줘.
총합은 100이 되어야 하며, 소수점은 한 자리까지만 표시해.

문장: "{text}"

출력 예시:
{{"상냥함": 70.5, "분노": 10.0, "유머": 19.5}}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 감정 분석 전문가입니다."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=150,
        n=1
    )
    try:
        result_text = response.choices[0].message.content.strip()
        result_dict = json.loads(result_text)
        return result_dict
    except Exception as e:
        st.error(f"분석 중 오류가 발생했습니다: {e}")
        return None

# ——— 분석 버튼 및 실행 ———
if st.button("🔮 분석 시작"):
    if not user_text.strip():
        st.warning("분석할 문장을 입력해주세요!")
    else:
        with st.spinner("GPT가 말투를 분석 중입니다... 잠시만 기다려주세요 ⏳"):
            result = analyze_tone_ai(user_text)
        if result:
            st.success("✅ 분석 완료!")
            col1, col2, col3 = st.columns(3, gap="large")

            # 컬러 & 이모지 맵핑
            mapping = {
                "상냥함": ("😇", "#4CAF50"),
                "분노": ("😡", "#E53935"),
                "유머": ("😂", "#FFC107")
            }

            # 숫자 크게 표시
            for col, emotion in zip([col1, col2, col3], result.keys()):
                emoji, color = mapping[emotion]
                col.markdown(f"<h2 style='text-align:center; color:{color}; font-weight:900;'>{emoji} {emotion}</h2>", unsafe_allow_html=True)
                col.markdown(f"<p style='font-size: 4rem; text-align:center; color:{color}; font-weight:bold; margin-top:0;'>{result[emotion]}%</p>", unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("<h3 style='text-align:center;'>📊 감정 비율 시각화</h3>", unsafe_allow_html=True)
            st.bar_chart(result)
