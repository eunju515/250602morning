import streamlit as st

st.title("💼 MBTI 기반 어울리는 직업 추천")

# MBTI 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

# MBTI 별 추천 직업 데이터
mbti_jobs = {
    "INTJ": [
        ("데이터 과학자", "분석적 사고와 장기적인 전략 설계에 강해요."),
        ("전략 컨설턴트", "논리적인 판단력으로 문제 해결에 탁월합니다."),
    ],
    "INFP": [
        ("작가", "감성과 상상력이 풍부해 글로 감정을 전달하는 데 능해요."),
        ("상담사", "타인의 감정을 공감하고 위로할 수 있어요."),
    ],
    "ENFP": [
        ("마케터", "창의적이고 사람들과 소통하는 것을 즐깁니다."),
        ("스타트업 창업자", "새로운 아이디어로 세상을 바꾸고 싶어해요."),
    ],
    "ISTJ": [
        ("회계사", "신중하고 책임감이 강해 정밀한 업무에 적합해요."),
        ("공무원", "체계적인 시스템과 규칙을 잘 따릅니다."),
    ],
    "ESFP": [
        ("MC/엔터테이너", "사람들 앞에서 에너지를 발산하는 데 탁월해요."),
        ("이벤트 플래너", "행사를 기획하고 사람을 즐겁게 해주는 걸 좋아해요."),
    ],
    # ... 다른 MBTI도 계속 확장 가능
}

# 결과 출력
if selected_mbti in mbti_jobs:
    st.subheader(f"🌟 {selected_mbti} 유형에게 어울리는 직업")
    for job, desc in mbti_jobs[selected_mbti]:
        st.markdown(f"- **{job}**: {desc}")
else:
    st.warning("해당 MBTI 유형에 대한 직업 정보가 아직 등록되지 않았어요.")
