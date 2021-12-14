import shortuuid
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd



st.title('Nube de palabras LinkedIn ☁️')


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     df_shares = pd.read_csv(uploaded_file)
        
texto_de_publicaciones = df_shares['ShareCommentary']
texto_de_publicaciones = [i for i in texto_de_publicaciones if type(i) == str]

# Obtengo la lista de stopwords (conectores, preposiciones, etc) en espanol gracias a nltk

nltk.download('stopwords')
stop_words = stopwords.words('spanish')
     

pressed = st.button('Apretame para generar los links')
if pressed:
   st.write(generar_links_exp(links))
