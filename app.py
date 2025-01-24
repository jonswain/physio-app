"""Streamlit app for physio exercises"""

import random
import time

import streamlit as st

delay = st.number_input("Select delay", min_value=1, max_value=10, value=3)
timer = st.number_input("Select exercise time", min_value=1, max_value=60, value=30)
directions = ["⬆️", "⬇️", "⬅️", "➡️"]

if st.button("Go"):
    placeholder = st.empty()

    # Countdown
    for i in range(3, 0, -1):
        placeholder.markdown(
            f"<h1 style='font-size:40px; text-align:center;'>{i}</h1>",
            unsafe_allow_html=True,
        )
        time.sleep(1)

    # Exercise loop
    end_time = time.time() + timer
    while time.time() < end_time:
        placeholder.markdown(
            f"<h1 style='font-size:40px; text-align:center;'>{"🟥"}</h1>",
            unsafe_allow_html=True,
        )
        time.sleep(0.1)
        placeholder.markdown(
            f"<h1 style='font-size:40px; text-align:center;'>{random.choice(directions)}</h1>",
            unsafe_allow_html=True,
        )
        time.sleep(delay - 0.1)
