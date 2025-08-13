import streamlit as st
import openai
import json

# OpenAI API 키 (streamlit secrets 사용 권장)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 페이지 설정
st.set_page_config(
    page_title="✨ AI 말투 분석기 ✨",
    page_icon="🗣️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# CSS 스타일링
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
        min-height: 100vh;
        padding: 3rem 2rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .title {
        font-size: 3rem;
        font-weight: 900;
        color: #4B0082;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px #aaa;
    }
    .subtitle {
        font-size: 1.25rem;
        text-align: center;
        color: #333333cc;
        margin-bottom: 2rem;
        font-weight: 600;
    }
    .footer {
        font-size: 0.85rem;
        color: #777;
        text-align: center;
        margin-top: 3rem;
    }
    .stButton>button {
        background: #4B0082;
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        box-shadow: 0 4px 15px rgba(75, 0, 130, 0.5);
        transition: background 0.3s ease;
    }
    .stButton>button:hover {
        background: #6a00d2;
        box-shadow: 0 6px 20px rgba(106, 0, 210, 0.7);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 앱 본문 HTML 래퍼
st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown('<h1 class="title">✨ AI 말투 분석기 🗣️</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">문장을 입력하면 GPT가 분노😡, 상냥함😇, 유머😂 비율을 세밀하게 분석해드립니다.</p>', unsafe_allow_html=True)

# 사용자 입력창
user_text = st.text_area(
    "문장을 입력해주세요 ✍️",
    placeholder="예: 안녕하세요! 오늘 기분 어때요? ㅋㅋ",
    height=150
)

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
        max_tokens=150
    )
    try:
        result_text = response.choices[0].message.content.strip()
        result_dict = json.loads(result_text)
        return result_dict
    except Exception as e:
        st.error(f"분석 중 오류가 발생했습니다: {e}")
        return None

if st.button("🔍 분석 시작"):
    if user_text.strip() == "":
        st.warning("문장을 입력해주세요!")
    else:
        with st.spinner("AI가 말투를 분석 중입니다... 잠시만 기다려주세요 ⏳"):
            result = analyze_tone_ai(user_text)

        if result:
            st.success("✅ 분석 완료!")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(f"<h3 style='color:#4CAF50; text-align:center;'>😇 상냥함</h3>", unsafe_allow_html=True)
                st.markdown(f"<h1 style='color:#4CAF50; text-align:center;'>{result['상냥함']}%</h1>", unsafe_allow_html=True)

            with col2:
                st.markdown(f"<h3 style='color:#E53935; text-align:center;'>😡 분노</h3>", unsafe_allow_html=True)
                st.markdown(f"<h1 style='color:#E53935; text-align:center;'>{result['분노']}%</h1>", unsafe_allow_html=True)

            with col3:
                st.markdown(f"<h3 style='color:#FFC107; text-align:center;'>😂 유머</h3>", unsafe_allow_html=True)
                st.markdown(f"<h1 style='color:#FFC107; text-align:center;'>{result['유머']}%</h1>", unsafe_allow_html=True)

            st.markdown("---")

            st.markdown("### 📊 시각화")
            st.bar_chart(result)

st.markdown('</div>', unsafe_allow_html=True)

# 풋터
st.markdown('<div class="footer">Made with ❤️ by ChatGPT</div>', unsafe_allow_html=True)
