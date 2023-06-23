import streamlit as st
from PIL import Image
import openai


openai.api_key = st.secrets["chat_gpt_key"]

def openai_response(query):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages = [
    {"role":"system", "content":"You are helpful assistant."},
    {"role":"user","content": query}
    ],
    temperature = 0.6,
    )
  return response.choices[0]['message']['content']  




with st.form("form"):

  url = st.text_input("URL")
  query = st.text_input("Query")
  submitted = st.form_submit_button("Submit")
  
  if submitted:
    response = openai_response(f"""Please analyse graph at this URL: {url} and {query}""")
    st.image(url)
    st.markdown(response)

