# Importamos 
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from wordcloud import WordCloud

# Para obtener la lista de "stopwords" y asi descartarlas
import nltk
from nltk.corpus import stopwords

#Generación de lista de signos de puntuación
import string  


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
