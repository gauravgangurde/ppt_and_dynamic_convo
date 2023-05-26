import streamlit as st
import pandas as pd
import numpy as np
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from PIL import Image

image = Image.open('exl.png')


llm = OpenAI(api_token=st.secrets["chat_gpt_key"])
pandas_ai = PandasAI(llm, conversational=False)

df = pd.read_csv('employees.csv')


with st.sidebar:
    st.image(image, caption='EXL')
    st.header('Conversational BI')
    st.write('Ask any question on your BI report')
    
st.header("BI Report (Structure)")
st.dataframe(df.head())

with st.form("my_form"):
   #st.write("Enter a question")
   #slider_val = st.slider("Form slider")
   #checkbox_val = st.checkbox("Form checkbox")
   query = st.text_input(label ="Enter a question" , placeholder = 'Enter your query')
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       response = pandas_ai_run(df, query)
       st.text(response)


