import streamlit as st
from PIL import Image

if "odr_val" not in st.session_state:
    st.session_state["odr_val"] = 0
if "confirm_order" not in st.session_state:
    st.session_state["confirm_order"] = False
if "bill_paid" not in st.session_state:
    st.session_state["bill_paid"] = False

menu = {
    "Pizza" : 750,
    "Burger" : 450,
    "Cold Drink" : 120,
    "fries" : 200}
odr_val = 0

col1, col2 = st.columns(2)
with col1:
    st.title("Welcome to our Restaurant!")
    with st.expander("Menu Bar :"):
        for item, price in menu.items():
            st.write(f"{item} : {price}")
    
    user_c = st.selectbox("Select the item that you want to order :", ("Pizza", "Burger", "Cold Drink", "fries"))
    button = st.button("Confirm Order")

    if button:
        st.session_state["odr_val"] += menu[user_c]
        st.session_state["confirm_order"] = True
        st.write(f"**Your Order of {user_c} is being processing.**")

with col2:
    img = st.image("grilled-beef-burger-with-fries-cheese-tomato-generative-ai.jpg", width=350)
    if st.session_state["confirm_order"]:
        with st.expander("Click to see your Bill that you have to pay:"):
            st.write(f"{st.session_state['odr_val']} Rupees only")

        bill = st.text_input("Pay the bill here :")
        button2 = st.button("Pay")
        if button2 :
            if bill:
                try:
                    bill=int(bill)
                    if bill == st.session_state["odr_val"]:
                        st.write("**Bill Paid. Thanks for visiting.**")
                        st.session_state["bill_paid"] = True
                    elif bill > st.session_state["odr_val"]:
                        st.write("Error! You have entered more than the bill amount.")
                    elif bill < st.session_state["odr_val"]:
                        st.write("Error! You have entered less than the bill amount")
    
                except ValueError:
                    st.write("Invalid Input! Please enter a numeric Value.")

            else:
                    st.write("Please enter a valid bill amount.")

        # if st.session_state["bill_paid"]:
        #     st.subheader("**Thanks for Visiting.**")


        

