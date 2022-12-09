import streamlit as st
import pandas as pd
import numpy as np
import joblib
import gdown

@st.cache(allow_output_mutation=True)
def load_model():
    url = 'https://drive.google.com/uc?id=1n_CObRNFjYx360I6D5r0lcUFZiU5JkCG'
    output = 'model.pkl'
    gdown.download(url, output, quiet=True)
    model = joblib.load('model.pkl')
    return model