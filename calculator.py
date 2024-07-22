import streamlit as st

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

st.title("Simple Calculator App")

operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])
a = st.number_input("Enter first number", step=1.0)
b = st.number_input("Enter second number", step=1.0)

if st.button("Calculate"):
    if operation == "Add":
        result = add(a, b)
    elif operation == "Subtract":
        result = sub(a, b)
    elif operation == "Multiply":
        result = mul(a, b)
    elif operation == "Divide":
        result = div(a, b)
    st.write("Result:", result)
