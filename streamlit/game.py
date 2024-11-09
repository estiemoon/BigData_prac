import streamlit as st
import random

st.title("rock scissors paper")
# ['✊🏿', '✌🏿','✋🏿']

idx = {'바위':'✊🏿','가위':'✌🏿','보':'✋🏿'}
choices = ['가위','바위','보']

user = st.selectbox('가위바위보', choices)


def comput(user):
    com = random.choice(choices)
    st.write(f"user: {idx[user]}")
    st.write(f"computer: {idx[com]}")
    
    if user == com:
        result = "무승부"
    elif (user == "가위" and com == "보") or \
        (user == "바위" and com == "가위") or \
        (user == "보" and com == "바위"):
        result = "당신이 이겼습니다! 🎉"
    else:
        result = "컴퓨터가 이겼습니다! 😢"

    st.text(result)
    
    return



st.button('결과확인',on_click=comput, args=[user])



# if st.button("새 게임 시작"):
#     st.rerun()


