import streamlit as st

st.title("三立食品 食品衛生クイズアプリ")

question = "食品を安全に保存するための適切な温度は？"
options = ["0〜5℃", "10〜15℃", "20〜25℃"]
answer = "0〜5℃"

user_answer = st.radio("Q1: " + question, options)

if st.button("回答する"):
    if user_answer == answer:
        st.success("正解！その通り！🎉")
    else:
        st.error("残念、不正解！正しくは「0〜5℃」だよ。")
