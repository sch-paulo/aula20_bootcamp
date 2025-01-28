import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout='wide')

st.image('logo.png', width=200)

st.title('Gerenciamento de produtos')

# Função auxiliar para exibir mensagens de erro detalhadas