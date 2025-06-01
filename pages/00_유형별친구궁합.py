import streamlit as st

st.title("💖 MBTI 친구 궁합 테스트")

# MBTI 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 사용자 MBTI 입력
user1_mbti = st.selectbox("👤 친구 1의 MBTI를 선택하세요", mbti_types, key="user1")
user2_mbti = st.selectbox("👥 친구 2의 MBTI를 선택하세요", mbti_types, key="user2")

# 간단한 궁합 데이터 (예시)
mbti_match_data = {
    ("INFP", "ENFJ"): {
        "score": 95,
        "desc": "감성과 논리가 조화를 이루는 최고의 궁합이에요!",
        "tip": "서로 감정을 존중하면 오래갈 수 있어요 💞"
    },
    ("INTJ", "ENFP"): {
        "score": 90,
        "desc": "이성적인 INTJ와 열정적인 ENFP, 서로의 부족함을 채워줘요.",
        "tip": "서로의 차이를 이해하려는 노력이 중요해요!"
    },
    ("ISTJ", "ESFP"): {
        "score": 60,
        "desc": "정반대의 성향이지만, 반대로 매력을 느낄 수도 있어요.",
        "tip": "서로의 라이프스타일을 존중해보세요 😅"
    },
    # 기본값이 될 수 있는 항목도 추가
}

# 결과 보여주기
if st.button("🔍 궁합 확인하기"):
    pair = (user1_mbti, user2_mbti)
    reverse_pair = (user2_mbti, user1_mbti)
    
    if pair in mbti_match_data:
        result = mbti_match_data[pair]
    elif reverse_pair in mbti_match_data:
        result = mbti_match_data[reverse_pair]
    else:
        result = {
            "score": 70,
            "desc": "서로 다른 만큼 배울 게 많아요!",
            "tip": "다름을 인정하면 관계가 더 깊어질 거예요 💡"
        }

    st.subheader("🎯 궁합 결과")
    st.write(f"**궁합 점수:** {result['score']}점")
    st.write(f"**설명:** {result['desc']}")
    st.info(result["tip"])
