import streamlit as st
import folium
from streamlit_folium import st_folium
from PIL import Image
import base64

# 페이지 설정
st.set_page_config(page_title="한국 여행 가이드", page_icon="🌏", layout="wide")

# 여행지 데이터
travel_data = [
    {
        "name": "경복궁",
        "region": "서울",
        "lat": 37.579617,
        "lon": 126.977041,
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/37/Gyeongbokgung_Gwanghwamun_gate.jpg",
        "description": "조선 시대의 정궁으로, 고궁 투어와 한복 체험으로 유명합니다."
    },
    {
        "name": "해운대 해수욕장",
        "region": "부산",
        "lat": 35.158698,
        "lon": 129.160384,
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Haeundae_Beach.jpg",
        "description": "한국을 대표하는 해변으로, 여름철 피서지로 인기가 높습니다."
    },
    {
        "name": "불국사",
        "region": "경주",
        "lat": 35.790144,
        "lon": 129.331504,
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/df/Bulguksa_Temple_2011.JPG",
        "description": "세계문화유산으로 지정된 신라 시대의 대표 사찰입니다."
    },
    {
        "name": "성산일출봉",
        "region": "제주",
        "lat": 33.458759,
        "lon": 126.941402,
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Seongsan_Ilchulbong.JPG",
        "description": "화산 활동으로 생긴 제주의 명소이며, 일출이 아름답기로 유명합니다."
    }
]

# 사이드바
st.sidebar.title("🔍 여행지 필터")
regions = ["전체"] + sorted(set([place["region"] for place in travel_data]))
selected = st.sidebar.selectbox("지역 선택", regions)

# 타이틀
st.markdown("""
    <h1 style='text-align: center; color: #2C3E50;'>🇰🇷 한국 여행 가이드</h1>
    <p style='text-align: center; font-size: 18px;'>아름다운 한국의 명소를 소개합니다. 지도를 클릭하거나, 아래에서 사진과 설명을 확인해보세요.</p>
""", unsafe_allow_html=True)

# 지도 초기화
m = folium.Map(location=[36.5, 127.8], zoom_start=7, tiles="CartoDB positron")

# 필터링
if selected != "전체":
    filtered_data = [place for place in travel_data if place["region"] == selected]
else:
    filtered_data = travel_data

# 지도에 마커 추가
for place in filtered_data:
    html = f"""
        <div style='width:200px;'>
            <h4>{place['name']}</h4>
            <img src='{place['image']}' width='100%'><br>
            <p>{place['description']}</p>
        </div>
    """
    folium.Marker(
        location=[place["lat"], place["lon"]],
        tooltip=place["name"],
        popup=folium.Popup(html, max_width=250)
    ).add_to(m)

# 지도 출력
st_data = st_folium(m, width=900, height=500)

# 여행지 카드 스타일 출력
st.markdown("## 📍 추천 여행지")
for place in filtered_data:
    st.markdown(f"""
        <div style='display: flex; gap: 20px; padding: 15px; margin-bottom: 20px; background-color: #f8f9fa; border-radius: 15px;'>
            <img src='{place['image']}' width='300px' style='border-radius: 10px;'>
            <div>
                <h3 style='margin-bottom: 5px;'>{place['name']} <span style='font-size: 16px; color: gray;'>({place['region']})</span></h3>
                <p style='font-size: 16px;'>{place['description']}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <hr style='margin-top: 40px;'>
    <p style='text-align: center; font-size: 14px; color: gray;'>Copyright © 2025 Travel Korea</p>
""", unsafe_allow_html=True)
