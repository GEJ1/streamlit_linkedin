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


def generar_nube_de_palabras(input, uploded_file = None):  
  """
  Funcion para hacer la nube de palabras en base a un .csv especifico que tenga una columna "ShareCommentary" como se encuentra
  en el archivo Share.csv que nos proporciona LinkedIn
  
  Parameters
  ------------------
  input        -> Para decidir si se usa el 'template' o se toma el archivo cargandolo ('file')
  uploded_file -> Informacion el csv cargado
  
  
  Returns
  ------------------
  None
  """
  if input == 'file':
    df_shares = pd.read_csv(uploded_file)
  elif input == 'template':
    url = 'https://gist.githubusercontent.com/GEJ1/a9b95be7c3700f65650fa2266210a65a/raw/66306eb5da836ce37c957b376632e900b0b2d716/Shares.csv'
    df_shares = pd.read_csv(url)
    
  texto_de_publicaciones = df_shares['ShareCommentary']
  texto_de_publicaciones = [i for i in texto_de_publicaciones if type(i) == str]

  # Uso set para borrar repetidos
  texto = [i for i in set(texto_de_publicaciones) if type(i) == str]

  texto = ''.join(texto)

  # Limpiamos
  clean_texto = limpiar_puntuacion_stopwords(texto)

  # Hacemos el wordcloud
  word_cloud = WordCloud(height=800, width=800, background_color='white',max_words=100, min_font_size=5).generate(clean_texto)
  fig, ax = plt.subplots()

  # Sacamos los ticks de los ejes 
  ax.axis('off')

  ax.imshow(word_cloud)
  title_alignment = """
  <style> #the-title { 
  text-align: center
  }
  </style>"""

  st.markdown(title_alignment, unsafe_allow_html=True)

  st.title("Tu nube de palabras 😀")
  fig  # 👈 Draw a Matplotlib chart

  st.image(
  "https://cdn-icons-png.flaticon.com/512/174/174857.png",
  width= 60, # Manually Adjust the width of the image as per requirement
  )

  st.markdown('''
  ## Espero que te haya gustado!
  ### El código de la App podés verlo [entrando acá](https://github.com/GEJ1/streamlit_linkedin) 
  ### Si te interesa la Ciencia de Datos y Python podés seguirme en [LinkedIn](https://www.linkedin.com/in/gustavo-juantorena/) y [Github](https://github.com/GEJ1)
  ''')

# Obtengo la lista de stopwords (conectores, preposiciones, etc) en espanol gracias a nltk
nltk.download('stopwords')
stop_words = stopwords.words('spanish')


st.title('☁️ Nube de palabras LinkedIn ☁️')

st.markdown("Si queres ver un ejemplo sin usar tus datos presioná el siguiente botón")      
pressed = st.button('Ver ejemplo')

# Cargamos template
if pressed:
   generar_nube_de_palabras('template')
    
st.subheader('Subí el archivo que te proporciona LinkedIn con la info de lo que compartiste (se llama "Shares.csv")')
st.markdown("*Podés ver las instrucciones para obtener tus datos de LinkedIn [entrando acá](https://gist.github.com/GEJ1/68a7525f6e38a074f1474db3e0f894d6)*")
uploaded_file = st.file_uploader("Seleccioná el archivo")

# Cargamos desde archivo
if uploaded_file is not None:
  generar_nube_de_palabras('file', uploaded_file)





   
