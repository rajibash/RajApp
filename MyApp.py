#def calExpensesExternal(data):
#    total = 0
#    for item in data:
#        value = item.get("amount")
#        total += value  # same as total = total +value
#    print(f"Your total expenses is {total}")

import streamlit as st

import pandas as pd

temp = [{"Temperature": "Feht", "value": 32}]
def tempConverter(data):
    tempCon = 0
    for item in data:
        Feht = item.get("value")
        tempCon = ((Feht - 32) * (5/9))
        print(f"My Temperature is {tempCon}")

        tempCon = input("Enter your temp")
    print(tempCon)
   
    st.set_page_config(page_title="Temperature Conerter",
                   page_icon="🔀")


# --- Title----

st.subheader("Temperature Converter")

tempConverter = {
    "Temperature": [],
    "Value": []
}

with st.form(key="form", clear_on_submit=True):
    Temperature = st.text_input('Enter your Temperature')
    value = st.number_input('Enter the valuerun')
    add_btn = st.form_submit_button("Add", type="primary")

# Event handler
def tempConverter(Temperature, value):
    if Temperature and value:
        temp.get('Temperature').append(Temperature)
        temp.get("value").append(value)


if add_btn:
    tempConverter(Temperature=Temperature, value=value)

# Create a DataFrame Object
df = pd.DataFrame(temp)

# Display df as a table

if len(temp.get('Temperature')) > 0 and len(value.get('value')) > 0:
    st.table(df)

amounts_list = temp.get("value")
temp = [{"Temperature": "Feht", "value": 32}]

tempCon = 0
for item in temp:
        Feht = item.get("value")
        tempCon = ((value - 32) * (5/9))
        print(f"My Temperature is {tempCon}")

st.subheader(f'Your total expenses is: {tempCon}')
