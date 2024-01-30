import streamlit as st
import datetime
import pandas as pd
import numpy as np

st.balloons()


if st.button('"Give me ballon"'):
    st.balloons()


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

with st.form("my_form"):
    st.write("Inside the form")
    #slider_val = st.slider("Form slider")
    title = st.text_input("What's your name")
    checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
st.image('cat.jpg')
st.write('Hello, *World!* :sunglasses:')


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

#picture = st.camera_input("Take a picture")

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

