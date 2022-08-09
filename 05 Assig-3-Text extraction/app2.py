from PIL import Image
from pyparsing import Word
import streamlit as st
import boto3

st.title('Text recognition from Image using AWS')
img_file=st.file_uploader('Upload Face Image',type=['png','jpg','jpeg'])
madic=""
count=0

def load_img(img):
    img=Image.open(img)
    return img

if img_file is not None :
    file_details={}
    file_details['name']=img_file.name
    file_details['type']=img_file.type
    file_details['size']=img_file.size
    st.write(file_details)
    st.image(load_img(img_file),width=255)
    
    with open('input.jpg','wb') as f:
        f.write(img_file.getbuffer())

    Client=boto3.client('rekognition')
    imageSource=open('input.jpg','rb')
    response=Client.detect_text(
    Image={'Bytes': imageSource.read()})
    textDetections=response['TextDetections'] 
    st.write('Detected Text')
    for text in textDetections:
        if text['Type']=="LINE":
            ant=text['DetectedText']
            st.write(ant+"\n")
    #st.write(textDetections)
        #st.write('Confidence:'+"{:.2f}".format(text['Confidence'])+"%")
        #st.write('Id: {}'.format(text['Id']))
