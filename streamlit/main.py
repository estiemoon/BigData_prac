import streamlit as st
import pandas as pd

pages = {
    "chart": [
        st.Page("chart.py", title="차트 연습1"),
    ],
    "game": [
        st.Page("game.py", title="가위바위보 게임"),
    ],
}

pg = st.navigation(pages)
pg.run()





