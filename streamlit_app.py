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
    
    fig1, x1= plt.subplots()
    response1 = pandas_ai(df, prompt=f"Plot {graph1}")
    st.pyplot(fig1)
    fig1.savefig('graph1.jpg')

    fig2, x2= plt.subplots()
    response2 = pandas_ai(df, prompt=f"Plot {graph2}")
    st.pyplot(fig2)
    fig2.savefig('graph2.jpg')

    fig3, x3= plt.subplots()
    response3 = pandas_ai(df, prompt=f"Plot {graph3}")
    st.pyplot(fig3)
    fig3.savefig('graph3.jpg')

    fig4, x4= plt.subplots()
    response4 = pandas_ai(df, prompt=f"Plot {graph4}")
    st.pyplot(fig4)
    fig4.savefig('graph4.jpg')


    
    # Create a new PowerPoint presentation
    presentation = Presentation()
    
    # Define the image file paths
    image_paths = ['graph1.jpg', 'graph2.jpg', 'graph3.jpg', 'graph4.jpg']
    
    # Create a slide with a 2x2 image grid
    slide_layout = presentation.slide_layouts[6]  # Use slide layout with 2 content placeholders
    slide = presentation.slides.add_slide(slide_layout)
    shapes = slide.shapes
    left = presentation.slide_width * 0.01
    top = Ipresentation.slide_width * 0.01
    width = height = presentation.slide_width * 0.2
    
    # Iterate over the image paths and add images to the slide
    for i, image_path in enumerate(image_paths):
        if i > 3:
            break
        # Add image to the slide
        picture = shapes.add_picture(image_path, left, top, width, height)
        # Update positioning for the next image
        if i == 1:
            left = Inches(4.5)
        else:
            top = Inches(4.5)
        
        # Save the PowerPoint presentation
        presentation.save('image_grid.pptx')
    
    with open("image_grid.pptx", "rb") as file:
        st.download_button(
            label="Download data",
            data=file,
            file_name='image_grid.pptx'
            )
