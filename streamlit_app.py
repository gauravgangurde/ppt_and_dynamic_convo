import streamlit as st
import pandas as pd
import numpy as np
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from PIL import Image
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.util import Inches

image = Image.open('exl.png')


llm = OpenAI(api_token=st.secrets["chat_gpt_key"])
pandas_ai = PandasAI(llm, conversational=False)#, enforce_privacy = True)

df = pd.read_csv('data.csv')
    
with st.sidebar:
    st.image(image, width = 150)
    st.header('Graphs')
    st.write('Create 2*2 graph grid')


st.subheader("Data" )
st.dataframe(df.head())

graph1 = st.text_input(label ="Graph1")
graph2 = st.text_input(label ="Graph2")
graph3 = st.text_input(label ="Graph3")
graph4 = st.text_input(label ="Graph4")

if st.button("Submit"):
    
    fig1, x1= plt.subplots()
    response1 = pandas_ai(df, prompt=f"Plot {graph1}")
    #st.pyplot(fig1)
    fig1.savefig('graph1.png')

    fig2, x2= plt.subplots()
    response2 = pandas_ai(df, prompt=f"Plot {graph2}")
    #st.pyplot(fig2)
    fig2.savefig('graph2.png')

    fig3, x3= plt.subplots()
    response3 = pandas_ai(df, prompt=f"Plot {graph3}")
    #st.pyplot(fig3)
    fig3.savefig('graph3.png')

    fig4, x4= plt.subplots()
    response4 = pandas_ai(df, prompt=f"Plot {graph4}")
    #st.pyplot(fig4)
    fig4.savefig('graph4.png')


    
    # Create a new PowerPoint presentation
    presentation = Presentation()
    
    # Define the image file paths
    image_paths = ['graph1.png', 'graph2.png', 'graph3.png', 'graph4.png']
    
    # Create a slide with a 2x2 image grid
    slide_layout = presentation.slide_layouts[6]  # Use slide layout with 2 content placeholders
    slide = presentation.slides.add_slide(slide_layout)
    shapes = slide.shapes
    # Define the dimensions of each graph
    width = Inches(4)
    height = Inches(3)
    
    # Add the first graph to the slide
    left = top = Inches(0.5)
    pic = slide.shapes.add_picture('graph1.png', left, top, width=width, height=height)
    
    # Add the second graph to the slide
    left = Inches(5.5)
    pic = slide.shapes.add_picture('graph2.png', left, top, width=width, height=height)

    # Add the third graph to the slide
    left = Inches(0.5)
    top = Inches(4)
    pic = slide.shapes.add_picture('graph3.png', left, top, width=width, height=height)
    
    # Add the fourth graph to the slide
    left = Inches(5.5)
    pic = slide.shapes.add_picture('graph4.png', left, top, width=width, height=height)

    
    presentation.save('image_grid.pptx')
    
    with open("image_grid.pptx", "rb") as file:
        st.download_button(
            label="Download data",
            data=file,
            file_name='image_grid.pptx'
            )
