import streamlit as st

import pandas as pd

import calendar

yy = 2024


st.set_page_config(page_title="Daily Hotel Sales",
                   page_icon="🖥")


st.subheader("Daily Sales Record")


with st.form(key="form", clear_on_submit=True):
    date = st.number_input("Enter today's date)
    roomNumber = st.text_input('Enter the room number')
    amount = st.number_input('Enter the Tamount paid')
    add_btn = st.form_submit_button("Add", type="primary")

Sales = 0

    # Event handler
def SalesCalculator(date, roomNumber, amount):
        if roomNumber and amount:
            Sales =+ amount
            Sales = round(Sales,2)
            print(f"The total sales for {date} is {Sales}")
            return f"The total sales for {date} is {Sales}"
            
if add_btn:
        display = SalesCalculator(roomNumber=roomNumber, amount=amount, date=date)
        st.subheader(display)

