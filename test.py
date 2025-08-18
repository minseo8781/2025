import streamlit as st
import random

st.set_page_config(page_title="🧳 여행 취향 테스트", page_icon="🌍", layout="centered")
st.title("🧳 여행 취향 테스트")
st.write("질문에 답하면 당신에게 어울리는 여행지를 추천하고, 가볼 만한 장소까지 알려드려요! ✨")

# -------------------- 질문 --------------------
q1 = st.radio("1️⃣ 자연환경 선호", ["🏔️ 산", "🏖️ 바다"])
q2 = st.radio("2️⃣ 계절 선호", ["☀️ 여름", "❄️ 겨울"])
q3 = st.radio("3️⃣ 여행 스타일", ["🏄‍♂️ 액티비티", "🛌 휴양"])
q4 = st.radio("4️⃣ 도시 vs 자연", ["🏙️ 도시", "🌲 자연"])

# -------------------- 여행지 데이터 --------------------
destinations = [
    {
        "name": "제주도",
        "tags": ["바다","여름","휴양","자연"],
        "image": "https://cdn.pixabay.com/photo/2017/03/28/12/10/jeju-2182873_1280.jpg",
        "description": "맑은 바다와 한라산이 어우러진 자연 휴양지입니다. 해수욕, 오름 트레킹, 카페 여행까지 즐길 수 있어요.",
        "spots": ["성산일출봉", "협재해수욕장", "한라산 등반", "제주 카페 거리"]
    },
    {
        "name": "스위스 알프스",
        "tags": ["산","겨울","액티비티","자연"],
        "image": "https://cdn.pixabay.com/photo/2018/03/01/10/03/swiss-3194321_1280.jpg",
        "description": "눈 덮인 산과 스키, 하이킹 등 액티비티 즐기기 좋은 겨울 여행지입니다.",
        "spots": ["융프라우요흐", "체르마트", "루체른 호수", "인터라켄"]
    },
    {
        "name": "몰디브",
        "tags": ["바다","여름","휴양","자연"],
        "image": "https://cdn.pixabay.com/photo/2016/12/06/18/27/maldives-1883333_1280.jpg",
        "description": "푸른 바다와 리조트에서 여유롭게 휴양을 즐기기 완벽한 섬입니다.",
        "spots": ["말레 수도", "바아 아톨 리조트", "다이빙 스팟", "산호섬 투어"]
    },
    {
        "name": "파리",
        "tags": ["도시","여름","휴양","도시"],
        "image": "https://cdn.pixabay.com/photo/2015/03/26/09/54/eiffel-tower-690293_1280.jpg",
        "description": "예술과 문화의 도시로 관광, 쇼핑, 카페 투어까지 즐길 수 있어요.",
        "spots": ["에펠탑", "루브르 박물관", "몽마르트 언덕", "샹젤리제 거리"]
    }
]

# -------------------- 추천 --------------------
if st.button("🌟 여행지 추천 받기"):
    user_tags = [
        "산" if q1=="🏔️ 산" else "바다",
        "여름" if q2=="☀️ 여름" else "겨울",
        "휴양" if q3=="🛌 휴양" else "액티비티",
        "도시" if q4=="🏙️ 도시" else "자연"
    ]

    matches = [d for d in destinations if all(tag in d["tags"] for tag in user_tags)]
    if matches:
        choice = random.choice(matches)
    else:
        choice = random.choice(destinations)

    # -------------------- 결과 표시 --------------------
    st.subheader(f"✈️ 추천 여행지: {choice['name']}")
    st.image(choice["image"], use_column_width=True)
    st.write(choice["description"])

    st.write("🏖️ 가볼 만한 장소 추천:")
    for spot in choice["spots"]:
        st.markdown(f"- {spot}")
