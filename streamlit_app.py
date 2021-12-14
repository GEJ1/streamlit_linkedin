import shortuuid
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd



st.title('Nube de palabras LinkedIn ☁️')

links = {
    'tmt_link': 'https://mbkhqarelc.cognition.run',
    'gonogo_link': 'https://mm9wnqlptd.cognition.run',
    'cdt_link': 'https://do2ptr4gcf.cognition.run',
    'stopsignal_link': 'https://u6t78zoibs.cognition.run'
  }

def generar_links_exp(links):
  """
  Genera un ID,  lo agrega a cada link definido en el diccionario "links" e imprime el resultado
  """
  id = shortuuid.uuid()
  queries = '?id=' 
  return (f"""
  El id es: {id}
  Los links a los experimentos son los siguientes:
   * TMT: {links['tmt_link']}{queries}{id}
   * GO NO GO: {links['gonogo_link']}{queries}{id}
   * CDT: {links['cdt_link']}{queries}{id}
   * STOP SIGNAL: {links['stopsignal_link']}{queries}{id}
  """)

# links = generar_links_exp(links)

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
     dataframe = pd.read_csv(uploaded_file)
     

pressed = st.button('Apretame para generar los links')
if pressed:
   st.write(generar_links_exp(links))
