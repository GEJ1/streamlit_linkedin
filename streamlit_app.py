# Importamos 
import streamlit as st
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
     # Can be used wherever a "file-like" object is accepted:
     df_shares = pd.read_csv(uploaded_file)
        
     texto_de_publicaciones = df_shares['ShareCommentary']
     texto_de_publicaciones = [i for i in texto_de_publicaciones if type(i) == str]

     # Obtengo la lista de stopwords (conectores, preposiciones, etc) en espanol gracias a nltk
     nltk.download('stopwords')
     stop_words = stopwords.words('spanish')

     # Uso set para borrar repetidos
     texto = [i for i in set(texto_de_publicaciones) if type(i) == str]

     texto = ''.join(texto)

     def limpiar_puntuacion_stopwords(texto):
       """
       Funcion para limpiar el string

       #Modificado de la siguiente fuente: https://antonio-fernandez-troyano.medium.com/nube-de-palabras-word-cloud-con-python-a-partir-de-varias-webs-111e94220822

       Parameters 
       ---------------
       texto (str)       -> Texto a limpiar

       Returns
       ---------------
       texto_limpio (str) -> Texto limpio luego de sacarle signos de puntuacion y stopwords

       """
       puntuacion = []
       for s in string.punctuation:
           puntuacion.append(str(s))
       sp_puntuacion = ["¿", "¡", "“", "”", "…", ":", "–", "»", "«"]    

       puntuacion += sp_puntuacion

       #Reemplazamos signos de puntuación por "":
       for p in puntuacion:
           texto_limpio = texto.lower().replace(p,"")

       for p in puntuacion:
           texto_limpio = texto_limpio.replace(p,"")

       #Reemplazamos stop_words por "":    
       for stop in stop_words:
           texto_limpio_lista = texto_limpio.split()
           texto_limpio_lista = [i.strip() for i in texto_limpio_lista]
           try:
               while stop in texto_limpio_lista: texto_limpio_lista.remove(stop)
           except:
               print("Error")
               pass
           texto_limpio= " ".join(texto_limpio_lista)

       return texto_limpio

     # Limpiamos
     clean_texto = limpiar_puntuacion_stopwords(texto)

     # Hacemos el wordcloud
     word_cloud = WordCloud(height=800, width=800, background_color='white',max_words=100, min_font_size=5).generate(clean_texto)

     # word_cloud.to_file("./img/ejemplo_sencillo.png") #Guardamos la imagen generada

     plt.figure(figsize=(10,8))
     plt.imshow(word_cloud)
     plt.axis('off')
     plt.tight_layout(pad=0)
     st.pyplot(word_cloud)


# pressed = st.button('Apretame para generar los links')
# if pressed:
#    st.write(generar_links_exp(links))
