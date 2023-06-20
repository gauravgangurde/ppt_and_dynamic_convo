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


tab1, tab2, tab3 = st.tabs(["Generate", "Convo", "Comparison"])

with tab1:
  if st.button("Reset"):
    with open('convo.txt', 'w') as file:
      file.write("Executive - Hello, How can I help you?\n")
    with open("temp.txt", 'w') as f:
      pass#f.write()
  
      
  with open("convo.txt", 'r') as file:
    convo = file.read()
  with open("temp.txt", 'r') as f:
    temp_customer = f.read()
    
  customer = st.text_input(label ="Customer")

  with st.form("form"):
    if customer != temp_customer:
      response = openai_response(f"""Conversation Between AIG executive and customer
                  {convo} customer- {customer} \n
                  Based on the above conversation, provide what the executive should say next?. Provide in follwing format
                  executive - <response>""")
      executive = st.text_area("Executive",height = 150, value= response)
      submitted = st.form_submit_button("Submit")
      if submitted:
        with open("temp.txt","w") as f:
          f.write(customer)

        with open('convo.txt', 'w') as file:
          file.write( f"""{convo}\n\nCustomer - {customer}\n\n{executive}""")

with tab2:
  with open("convo.txt", 'r') as file:
    convo_new = file.read()
  st.markdown(convo_new)

with tab3:
  with open('claims.txt', 'r') as file:
    ln = file.readlines()
  if st.button("Compare"):
    x = ''
    t = 0
    for i in range(4,len(ln),4):
      convo1 = ''.join(ln[:i])
      response1 = openai_response(f"""Conversation Between AIG executive and customer
                  {convo1}
                  Based on the above conversation, provide what the executive should say next?. Provide in follwing format
                  Executive - <response>""")
      x = f"""{x}\n{''.join(ln[t:i])}\n <hr><b>{response1}</b><hr>"""
      t = i+1
    with open("compare.txt", 'w') as file:
      file.write(x)
  with open("compare.txt","r") as file:
    res = file.read()
  st.markdown(res, unsafe_allow_html=True)
    

