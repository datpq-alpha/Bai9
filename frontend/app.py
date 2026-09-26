"""Giao diện Bài 9: tra cứu và quản lý thành phố yêu thích."""

import requests
import streamlit as st


API_URL = "http://localhost:8000"

st.set_page_config(page_title="Weather Favorites", page_icon="🌦️")
st.title("🌦️ Thời tiết và thành phố yêu thích")

search_tab, favorites_tab = st.tabs(["Tra cứu", "Đã lưu"])

with search_tab:
    city = st.text_input("Tên thành phố", placeholder="Ví dụ: Hanoi")

    if st.button("Xem thời tiết", type="primary"):
        if not city.strip():
            st.warning("Em hãy nhập tên thành phố.")
        else:
            try:
                response = requests.get(
                    f"{API_URL}/weather", params={"city": city.strip()}, timeout=10
                )
                if response.status_code == 200:
                    st.session_state["weather"] = response.json()
                else:
                    st.session_state.pop("weather", None)
                    st.error("Không tìm thấy thành phố.")
            except requests.RequestException:
                st.error("Không kết nối được tới backend.")

    if "weather" in st.session_state:
        data = st.session_state["weather"]
        st.success(data["city"])
        col1, col2 = st.columns(2)
        col1.metric("Nhiệt độ", f"{data['temp']} °C")
        col2.metric("Độ ẩm", f"{data['humidity']} %")
        st.write(data["description"].capitalize())

        if st.button(f"Lưu {data['city']}"):
            # TODO 5/5: POST tên thành phố lên /cities và báo kết quả cho người dùng.
            pass

with favorites_tab:
    try:
        response = requests.get(f"{API_URL}/cities", timeout=10)
        cities = response.json() if response.status_code == 200 else []
    except requests.RequestException:
        cities = []
        st.error("Không kết nối được tới backend.")

    if not cities:
        st.info("Chưa có thành phố nào được lưu.")
    else:
        st.subheader("Danh sách đã lưu")
        for item in cities:
            col_name, col_button = st.columns([3, 1])
            col_name.write(f"📍 {item['city_name']}")
            if col_button.button("Xóa", key=f"delete-{item['id']}"):
                result = requests.delete(
                    f"{API_URL}/cities/{item['city_name']}", timeout=10
                )
                if result.status_code == 200:
                    st.rerun()
                else:
                    st.error("Không xóa được thành phố.")

