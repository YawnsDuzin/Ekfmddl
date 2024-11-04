import pandas as pd
import numpy as np
import json

import folium
import streamlit as st
from streamlit_folium import st_folium


path_dateset = 'G:/내 드라이브/DataSet/'

# =========================================
# 데이터 불러오기
# - 자전거 대여소 정보
cols = ['대여소번호', '보관소(대여소)명', '자치구', '상세주소', '위도', '경도', '설치시기', '거치대수(LCD)', '거치대수(QR)', '운영방식']
# rental = pd.read_csv(path_dateset + '서울시 공공자전거 대여소 정보/공공자전거 대여소 정보(24.6월 기준).xlsx', encoding = 'utf-8', names = cols, index_col = False)
rental = pd.read_excel(path_dateset + '_최종 병합 파일\서울시 공공자전거 대여소 정보/공공자전거 대여소 정보(24.6월 기준).xlsx', sheet_name='대여소현황', names = cols)
rental = rental.iloc[4:]
rental.reset_index(drop = True, inplace = True)
# # - 자전거 도로 정보
geo_path = path_dateset + '_최종 병합 파일\\서울시 자전거 도로 데이터\\' + 'ddareng_road.geojson'
# geo_str = json.load(open(geo_path, encoding='cp949'))
# encoding을 UTF-8로 지정
with open(geo_path, 'rt', encoding='utf-8') as f:
    geo_str = json.load(f)
# # =========================================


# 지도 생성
center = [37.541, 126.986]
# center on Liberty Bell, add marker
bike_map = folium.Map(location=center, zoom_start=13)
# 스타일 지정 예시 (선의 색상, 두께 등)
style = {
    'color': 'red',
    'weight': 3,
    'opacity': 0.7,
}

# 자전거 도로 표시
# GeoJSON 파일을 불러와 스타일 적용
folium.GeoJson(
    geo_str,
    # name='styled_line',
    name='geojson',
    #style_function=lambda x: style
).add_to(bike_map)

# # 자전거 대여소 표시
# for i, row in rental.iterrows():
#   folium.CircleMarker(
#       location = [row['위도'], row['경도']],
#       radius = 1,
#       fill = True,
#   ).add_to(bike_map)

st.title("따릉이 시각화")
st.dataframe(rental, height=200)
st.checkbox('chk')

button = st.button('버튼을 눌러보세요')
if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')
    
# call to render Folium map in Streamlit
st_data = st_folium(bike_map, width=2000, height=2000)