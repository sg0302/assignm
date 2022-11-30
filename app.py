import streamlit as st
title = "subtract 2 numbers"
st.set_page_config(page_title=title)

st.title('division of 2 numbers')

x = st.number_input('Enter first number')
y = st.number_input('Enter second number')
if y!=0:
  z=x/y
  st.write(z,"is the result")
else:
  st.write('not defined')
