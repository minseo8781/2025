import streamlit as st
import random

# 카테고리별 메뉴 (더 풍성하게!)
menus = {
    "한식": [
        ("김치찌개", "https://cdn.pixabay.com/photo/2021/11/01/12/34/kimchi-6761132_1280.jpg"),
        ("비빔밥", "https://cdn.pixabay.com/photo/2017/06/19/20/23/bibimbap-2410514_1280.jpg"),
        ("불고기", "https://cdn.pixabay.com/photo/2016/03/05/19/02/bulgogi-1239356_1280.jpg"),
        ("삼겹살", "https://cdn.pixabay.com/photo/2017/07/16/10/43/pork-belly-2506399_1280.jpg"),
        ("갈비탕", "https://cdn.pixabay.com/photo/2016/06/28/17/02/soup-1483560_1280.jpg"),
        ("잡채", "https://cdn.pixabay.com/photo/2017/08/14/15/20/japchae-2649272_1280.jpg")
    ],
    "양식": [
        ("피자", "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_1280.jpg"),
        ("파스타", "https://cdn.pixabay.com/photo/2017/01/22/19/20/pasta-2007379_1280.jpg"),
        ("스테이크", "https://cdn.pixabay.com/photo/2016/03/05/19/02/steak-1239180_1280.jpg"),
        ("햄버거", "https://cdn.pixabay.com/photo/2014/10/23/18/05/burger-500054_1280.jpg"),
        ("샐러드", "https://cdn.pixabay.com/photo/2016/04/06/17/11/salad-1311490_1280.jpg"),
        ("리조또", "https://cdn.pixabay.com/photo/2017/05/07/08/56/risotto-2293449_1280.jpg")
    ],
    "중식": [
        ("짜장면", "https://cdn.pixabay.com/photo/2017/02/23/19/38/noodles-2090531_1280.jpg"),
        ("짬뽕", "https://cdn.pixabay.com/photo/2015/08/11/22/08/soup-884630_1280.jpg"),
        ("탕수육", "https://cdn.pixabay.com/photo/2016/09/06/20/33/chinese-food-1648749_1280.jpg"),
        ("마라탕", "https://cdn.pixabay.com/photo/2020/07/21/06/49/malatang-5423257_1280.jpg"),
        ("꿔바로우", "https://cdn.pixabay.com/photo/2017/08/06/11/19/chinese-food-2596089_1280.jpg"),
        ("깐풍기", "https://cdn.pixabay.com/photo/2015/06/15/15/39/chinese-food-810436_1280.jpg")
    ],
    "분식": [
        ("떡볶이", "https://cdn.pixabay.com/photo/2021/06/27/12/27/tteokbokki-6369625_1280.jpg"),
        ("순대", "https://cdn.pixabay.com/photo/2017/07/16/10/43/korean-food-2506398_1280.jpg"),
        ("김밥", "https://cdn.pixabay.com/photo/2017/07/16/10/44/kimbap-2506401_1280.jpg"),
        ("라면", "https://cdn.pixabay.com/photo/2016/11/18/15/11/ramen-1834539_1280.jpg"),
        ("오뎅탕", "https://cdn.pixabay.com/photo/2017/01/31/13/05/oden-2029177_1280.jpg"),
        ("치즈돈까스", "https://cdn.pixabay.com/photo/2019/06/10/07/44/pork-cutlet-4264741_1280.jpg")
    ],
    "일식": [
        ("초밥", "https://cdn.pixabay.com/photo/2017/05/07/08/56/sushi-2293488_1280.jpg"),
        ("라멘", "https://cdn.pixabay.com/photo/2017/06/06/09/53/ramen-2377753_1280.jpg"),
        ("돈부리", "https://cdn.pixabay.com/photo/2017/12/09/08/19/donburi-3007399_1280.jpg"),
        ("규카츠", "https://cdn.pixabay.com/photo/2016/11/23/14/45/japanese-food-1850144_1280.jpg"),
        ("가라아게", "https://cdn.pixabay.com/photo/2018/02/23/14/08/karaage-3177626_1280.jpg"),
        ("우동", "https://cdn.pixabay.com/photo/2017/06/25/16/37/udon-2443023_1280.jpg")
    ]
}

st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍴")
st.title("🍴 오늘 뭐 먹지? 메뉴 랜덤 뽑기")
st.write("카테고리를 고르고 버튼을 눌러보세요! 😋")

# 카테고리 선택
category = st.selectbox("👉 메뉴 카테고리 선택", list(menus.keys()))

if st.button("랜덤 추천 받기 🎲"):
    menu, img_url = random.choice(menus[category])
    st.subheader(f"오늘의 추천 메뉴는 👉 **{menu}** 🍽️")
    st.image(img_url, caption=menu, use_column_width=True)
