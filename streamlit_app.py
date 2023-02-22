import streamlit as st

from PIL import Image
from gtts import gTTS
import easyocr
reader = easyocr.Reader(['en','bho',"bn",'hi','mr','te','ta']) # this needs to run only once to load the model into memory
# from pytesseract import pytesseract
from deep_translator import GoogleTranslator
# path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title('Multilingual Image Translator and Reader')
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

def pdf_to_text(Img_Language,image_path,Language):

    image_path = Image.open(image_path)
    # text = pytesseract.image_to_string(image_path,lang = Img_Language,config=path_to_tesseract)
    result = reader.readtext(image_path,detail = 0)
    text = " ".join(result)
    # text = " ".join(text.split())

    text = GoogleTranslator(source='auto', target=Language).translate(text) 
    myobj = gTTS(text=text, lang=Language,tld='co.in', slow=False) 
    myobj.save("test.wav") 
    return "test.wav",text


d1  =  {"Hindi":'hin','Marathi':'mar','English':'eng','Sanskrit':'san'}
d2  =  {"Hindi":'hi','Marathi':'mr','English':'en'}
lang1 = ['English',"Hindi",'Marathi','Sanskrit']
lang = ["Hindi",'Marathi','English']

choice1 = st.sidebar.selectbox("Image_Language",lang1)
choice2 = st.sidebar.selectbox("Translated_Language",lang)


if image_file is not None:

        # To See details
        file_details = {"filename":image_file.name, "filetype":image_file.type,
                        "filesize":image_file.size}
        
        st.image(image_file, caption='Sunrise by the mountains')
        # st.write(file_details)
        A,T = pdf_to_text(d1[choice1] ,image_file,d2[choice2])
        # img = Image.open(image_file)

        # pytesseract.tesseract_cmd = path_to_tesseract
        
        st.write(T)
        st.audio(A)
    
