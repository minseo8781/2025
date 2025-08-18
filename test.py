import streamlit as st
import random

st.set_page_config(page_title="🧳 여행 취향 테스트", page_icon="🌍", layout="centered")
st.title("🧳 여행 취향 테스트")
st.write("질문에 답하면 당신에게 어울리는 여행지를 추천해드립니다! ✨")

# 1. 질문
q1 = st.radio("1️⃣ 자연환경 선호", ["🏔️ 산", "🏖️ 바다"])
q2 = st.radio("2️⃣ 계절 선호", ["☀️ 여름", "❄️ 겨울"])
q3 = st.radio("3️⃣ 여행 스타일", ["🏄‍♂️ 액티비티", "🛌 휴양"])
q4 = st.radio("4️⃣ 도시 vs 자연", ["🏙️ 도시", "🌲 자연"])

# 2. 여행지 데이터 (사진 + 설명)
destinations = [
    {
        "name": "제주도, 한국",
        "tags": ["바다", "여름", "휴양", "자연"],
        "image": "https://cdn.pixabay.com/photo/2017/03/28/12/10/jeju-2182873_1280.jpg",
        "description": "맑은 바다와 한라산이 어우러진 자연 휴양지. 해수욕, 오름 트레킹, 카페 여행까지 즐길 수 있어요."
    },
    {
        "name": "스위스 알프스",
        "tags": ["산", "겨울", "액티비티", "자연"],
        "image": "https://cdn.pixabay.com/photo/2018/03/01/10/03/swiss-3194321_1280.jpg",
        "description": "눈 덮인 산과 스키, 하이킹 등 액티비티 즐기기 좋은 겨울 여행지."
    },
    {
        "name": "몰디브",
        "tags": ["바다", "여름", "휴양", "자연"],
        "image": "https://cdn.pixabay.com/photo/2016/12/06/18/27/maldives-1883333_1280.jpg",
        "description": "푸른 바다와 리조트에서 여유롭게 휴양을 즐기기 완벽한 섬."
    },
    {
        "name": "파리, 프랑스",
        "tags": ["도시", "여름", "휴양", "도시"],
        "image": "https://cdn.pixabay.com/photo/2015/03/26/09/54/eiffel-tower-690293_1280.jpg",
        "description": "예술과 문화의 도시. 관광, 쇼핑, 카페 투어까지 즐길 수 있어요."
    },
    {
        "name": "호주 골드코스트",
        "tags": ["바다", "여름", "액티비티", "자연"],
        "image": "https://cdn.pixabay.com/photo/2017/04/03/11/52/surfing-2203361_1280.jpg",
        "description": "서핑, 다이빙 등 액티비티를 즐길 수 있는 해변 도시."
    },
    {
        "name": "노르웨이 피오르",
        "tags": ["산", "겨울", "휴양", "자연"],
        "image": "https://cdn.pixabay.com/photo/2017/01/20/19/53/norway-1998850_1280.jpg",
        "description": "겨울 풍경과 피오르 투어, 오로라 관측까지 자연을 만끽할 수 있어요."
    }
]

# 3. 답변 기반 추천
if st.button("🌟 여행지 추천 받기"):
    user_tags = []
    user_tags.append("산" if q1=="🏔️ 산" else "바다")
    user_tags.append("여름" if q2=="☀️ 여름" else "겨울")
    user_tags.append("액티비티" if q3=="🏄‍♂️ 액티비티" else "휴양")
    user_tags.append("도시" if q4=="🏙️ 도시" else "자연")

    # 태그 매칭
    matches = [d for d in destinations if all(tag in d["tags"] for tag in user_tags)]
    
    # 매칭 없으면 랜덤으로 보여주기
    if matches:
        choice = random.choice(matches)
    else:
        choice = random.choice(destinations)

    st.subheader(f"✈️ 추천 여행지: {choice['name']}")
    st.image(choice["image"], use_column_width=True)
    st.write(choice["description"])
