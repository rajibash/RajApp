#def calExpensesExternal(data):
#    total = 0
#    for item in data:
#        value = item.get("amount")
#        total += value  # same as total = total +value
#    print(f"Your total expenses is {total}")

import streamlit as st

import pandas as pd


st.set_page_config(page_title="Temperature Converter",
                   page_icon="🔀")


# --- Title----

st.subheader("Temperature Converter")




with st.form(key="form", clear_on_submit=True):
    Location = st.text_input('Enter your Location')
    value = st.number_input('Enter the Temperature in Feht')
    add_btn = st.form_submit_button("Add", type="primary")

 

    # Event handler
    def tempConverter(Location, value):
        if Location and value:
            tempCon = ((value - 32) * (5/9))
            tempCon = round(tempCon,2)
            print(f"My Temperature is {tempCon}")
            return f"Your location Temperature is {tempCon} in celsius"
            


    if add_btn:
        display = tempConverter(Location=Location, value=value)
        st.subheader(display)


