import streamlit as st
from PIL import Image
import openai

image = Image.open('exl.png')

openai.api_key = st.secrets["chat_gpt_key"]

def openai_response(query):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
    {"role":"system", "content":"You are helpful assistant."},
    {"role":"user","content": query}
    ],
    temperature = 0.6,
    )
  return response.choices[0]['message']['content']  


with st.sidebar:
  st.image(image, width = 150)
  st.header('Dynamic Scripting')



if st.button("Reset"):
  with open('convo.txt', 'w') as file:
    file.write("Executive - Hello, How can I help you?\n")
  with open("temp.txt", 'w') as f:
    f.write('customer')

    
with open("convo.txt", 'r') as file:
  convo = file.read()
with open("temp.txt", 'r') as f:
  temp_customer = file.read()

st.markdown(convo)
  
customer = st.text_input(label ="Customer")

if customer != temp_customer:
  response = openai_response(f"""Conversation Between AIG executive and customer
              {convo} customer- {customer} \n
              Based on the above conversation, provide what the executive should say next?. Provide in follwing format
              executive - <response>""")
  executive = st.text_area("Executive",value= response)
  if st.button("Submit"):
    with open("temp.txt","w") as f:
      f.write(customer)
    with open('convo.txt', 'w') as file:
      file.write(f"""{convo} \n\ncustomer - {customer}\n\n {executive}\n""")
    
  
