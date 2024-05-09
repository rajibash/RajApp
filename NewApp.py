import streamlit as st

import pandas as pd

import calendar

from datetime import date

todays_date = date.today()

st.set_page_config(page_title="Daily Hotel Sales",
                   page_icon="🖥")


st.subheader("Hotel Sales Record")

with st.form(key="form", clear_on_submit=True):
    date = todays_date = date.today()
    roomNumber = st.text_input('Enter the room number')
    amount = st.number_input('Enter the amount paid')
    add_btn = st.form_submit_button("Add", type="primary")

Sales = 0

    # Event handler
def SalesCalculator(roomNumber, amount):
        if roomNumber and amount:
            Sales =+ amount
            Sales = round(Sales,2)
            print(f"The total sales is {Sales}")
            return f"The total sales is {Sales}"
          
date = today's_date = date.today()
st.subheader(date)

if add_btn:
        display = SalesCalculator(roomNumber=roomNumber, amount=amount)
        st.subheader(display)

