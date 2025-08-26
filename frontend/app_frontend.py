import streamlit as st
import requests

st.set_page_config(page_title="AI Text Summarizer", layout="wide")

st.title("AI Text Summarizer")
st.write("Введите текст и получите его краткую версию с помощью ИИ")

# Текстовое поле для ввода текста
text = st.text_area("Введите текст для суммаризации", height=250)

# Поля для настройки минимальной и максимальной длины summary
col1, col2 = st.columns(2)
with col1:
    min_len = st.number_input("Минимальная длина summary", min_value=10, max_value=500, value=40, step=10)
with col2:
    max_len = st.number_input("Максимальная длина summary", min_value=20, max_value=1000, value=100, step=10)

# Кнопка для отправки запроса
if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Пожалуйста, введите текст для суммаризации")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/summarize/",
                json={"text": text, "min_length": min_len, "max_length": max_len}
            )
            if response.status_code == 200:
                summary = response.json()["summary"]
                st.success("Суммаризация готова!")
                st.text_area("Результат:", value=summary, height=200)
            else:
                st.error(f"Ошибка сервера: {response.status_code}")
        except Exception as e:
            st.error(f"Не удалось подключиться к FastAPI серверу: {e}")
