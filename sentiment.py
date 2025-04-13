import streamlit as st
from PIL import Image
import os;
import google.generativeai as genai

#define gemini api key
os.environ["GOOGLE_API_KEY"]="AIzaSyAk3XfMjeiivTSZ9MYHNMmHetTV7GR_Ar0"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model=genai.GenerativeModel("gemini-2.0-flash")
#------------------------------------------------------


tab1 ,tab2=st.tabs(["Description","Sentiment Analysis App!"])

# tab1
with tab1:
    col1,col2,col3=st.columns([1,2,1],gap="medium")
    with col2:
        st.header("Anubhuti AI 🤖")
    col1,col2=st.columns([1,2],gap="medium")
    with col2:
       st.text("✨ An AI Project by Soumendu Das ✨")
    col1, col2, col3 = st.columns([1, 2, 1],gap="medium")  # Adjust the ratio if needed
    with col2:
        st.image("D:/project/sentiment_analysis/pic1.jpg",width=300)
    st.markdown("""🧠 Sentiment Analysis from Image — by Soumendu Das
Welcome to my AI-powered Sentiment Analysis App!
This tool allows you to detect emotions from images containing text — such as tweets, handwritten notes, memes, posters, and more.

You can choose one of the two options from the sidebar:

📷 Camera – Take a picture directly using your webcam.

📁 Upload File – Upload an image from your device.

Once an image is provided, the app:

Extracts the text content from the image.

Analyzes the emotion behind the message.

Displays one of the following emotion labels:
Angry, Happy, Sad, Fear, Surprise, Disgust, or Neutral.""")
    st.feedback("stars")

#tab2
with tab2:
      col1, col2, col3 = st.columns([1, 2, 1],gap="medium")  # Adjust the ratio if needed
      with col2:
          st.image("D:/project/sentiment_analysis/pic2.jpg",width=300)
      select = st.radio("Select one:", ["Camera","Upload file"])
      if(select=="Upload file") : uploaded_image=st.file_uploader("upload an image",type=["jpg","png","jpeg"])                                                         
      else : uploaded_image=st.camera_input("take picture")
      search_object="You are an emotion recognition expert. Analyze the text in this image and return only one emotion that best matches the sentiment. Choose only from: 😡Angry, 😃Happy, 😔Sad, 😨Fear, 😮Surprise, 🥸Disgust, or 🙂Neutral. Reply with only that one word — no explanation."
      if uploaded_image:
          image=Image.open(uploaded_image)
          col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratio if needed
          with col2:
           st.image(image, caption="Uploaded Image", width=200)
          with st.spinner("Detecting Emotion ....."):
           response=model.generate_content([
            search_object,
            image
            ])
           st.success(response.text)
    
