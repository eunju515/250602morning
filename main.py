import streamlit as st
import random
from datetime import date

# 오늘 날짜
today = date.today()

st.title("😂 MBTI 유형별 오늘의 밈")

# 사용자 MBTI 입력
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# 임의로 간단한 MBTI 밈 데이터 준비
mbti_memes = {
    "INTJ": ["images/intj_1.jpg", "images/intj_2.jpg"],
    "INFP": ["images/infp_1.jpg", "images/infp_2.jpg"],
    "ENFP": ["images/enfp_1.jpg", "images/enfp_2.jpg"],
    # 나머지도 유사하게 채워넣을 수 있어요!
}

# 오늘 날짜에 따라 밈 선택을 고정하거나 무작위 선택
if selected_mbti in mbti_memes:
    meme_list = mbti_memes[selected_mbti]
    daily_index = hash(str(today) + selected_mbti) % len(meme_list)
    selected_meme = meme_list[daily_index]
    
    st.subheader(f"{selected_mbti} 유형을 위한 오늘의 밈 🎁")
    st.image(selected_meme, caption=f"{selected_mbti} 전용 유머!", use_column_width=True)
else:
    st.warning("선택한 MBTI에 대한 밈이 아직 준비되지 않았어요!")

# 새로운 밈 버튼 (랜덤)
if st.button("새로운 밈 보여줘! 🔄"):
    if selected_mbti in mbti_memes:
        st.image(random.choice(mbti_memes[selected_mbti]), caption="랜덤 밈!", use_column_width=True)
