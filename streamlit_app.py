import streamlit as st
import pandas as pd
import numpy as np
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from PIL import Image
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.util import Inches

#st.set_option('deprecation.showPyplotGlobalUse', False)
image = Image.open('exl.png')


llm = OpenAI(api_token=st.secrets["chat_gpt_key"])
pandas_ai = PandasAI(llm, conversational=False)#, enforce_privacy = True)

df = pd.read_csv('data.csv')
    
with st.sidebar:
    st.image(image, width = 150)
    st.header('Conversational BI')
    st.write('Ask any question on your BI report')


st.subheader("Data" )
st.dataframe(df.head())

graph1 = st.text_input(label ="Graph1")
graph2 = st.text_input(label ="Graph2")
graph3 = st.text_input(label ="Graph3")
graph4 = st.text_input(label ="Graph4")

if st.button("Submit"):
    
    fig, x= plt.subplots(2,2)
    response1 = pandas_ai(df, prompt=f"Plot {graph1}")
    response2 = pandas_ai(df, prompt=f"Plot {graph2}")
    response3 = pandas_ai(df, prompt=f"Plot {graph3}")
    response4 = pandas_ai(df, prompt=f"Plot {graph4}")
    st.pyplot(fig[0,0])
    st.pyplot(fig[1,0])
    st.pyplot(fig[0,1])
    st.pyplot(fig[1,1])
    fig.savefig('graphs.png')


    
    # Create a new PowerPoint presentation
    presentation = Presentation()
    
    # Define the image file paths
    image_paths = ['graph1.jpg', 'graph2.jpg', 'graph3.jpg', 'graph4.jpg']
    
    # Create a slide with a 2x2 image grid
    slide_layout = presentation.slide_layouts[6]  # Use slide layout with 2 content placeholders
    slide = presentation.slides.add_slide(slide_layout)
    
    left = top = Inches(0.5)
    pic = slide.shapes.add_picture('graphs.png', left, top)
    
    # Saving the presentation
    presentatio.save('presentation.pptx')
    
    with open("image_grid.pptx", "rb") as file:
        st.download_button(
            label="Download data",
            data=file,
            file_name='image_grid.pptx'
            )

