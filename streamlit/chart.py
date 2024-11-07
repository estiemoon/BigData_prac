import streamlit as st
import pandas as pd


debt_ratios = pd.DataFrame({
                           'debt':[97, 70,67,60],
                           'equity':[3,30,33,40]},
                           columns=['debt','equity'],
                           index=['South Korea', 'Japan', 'US', 'Australia'])

def display_chart():
    st.bar_chart(data=debt_ratios,x_label='Country',y_label='ratio',color=["#E55729", "#02CFE6"])

st.button('자기자본비율',on_click=display_chart)


data = {'A': [1,2,3], 'B':[1,4,9]}
data = pd.DataFrame(data)

input_num = st.number_input("Insert a Number")

data.loc[data['A']==1, 'B'] = input_num

st.bar_chart(data.set_index('A'))


