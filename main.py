# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:03:08 2023

@author: Mian c
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

#loading the save file from main model
loaded_model = pickle.load(open('C:/Users/Mian c/Downloads/Deploying Deep Learning Model/trained_model.sav', 'rb'))

#creating a function for prediction
def promoters_prediction(loaded_model):

        lno = len(loaded_model)
        if loaded_model == 0.3:
            return 'Promoters'
        else:
            return 'Non-Promoters'

with st.sidebar:

    selected = option_menu('Main Menu',
                           ['HOME', 'PREDICTOR', 'EXAMPLE'],
                           icons=['house','search','list-task'],
                           default_index=0, styles={
                               "container": {"padding": "0!important", "background-color": "#A4A3A6"},
                               "icon": {"color": "orange", "font-size": "20px"},
                               "nav-link": {"font-size": "20px", "text-align": "centre", "margin": "0px",
                                            "--hover-color": "#eee"},
                               "nav-link-selected": {"background-color": "#78737D"},
                           })

if (selected == "HOME"):

    st.title("Web Server for Promoters Prediction !")

    st.write("We develop a novel two-layer deep learning model called PROCABLES, which discriminate DNA sequence as promoter or non-promoter in the first layer and strong or weak promoter in the second layer. The proposed method, first utilizes five distinct features such as word2vec, Position-specific tri-nucleotide propensity, electron-ion interaction pseudopotentials, k-spaced nucleotide pairs and trinucleotide composition to encode DNA sequence. Afterwards, a stacked framework is formed using convolutional neural network with bidirectional long-short-term memory (BiLSTM) using multi-view features to get advantage of deep models"
            )
    image = Image.open('Architecture.PNG')
    st.image(image, width=850)

elif selected == "PREDICTOR":
    st.title("Predict Sequence")
    input_seq = st.text_area('Input Sequence')

    diagnosis = ""

    # creating a button
    if st.button('Enter'):
        diagnosis = promoters_prediction([input_seq])

        st.success(diagnosis)

elif selected == "EXAMPLE":
    st.title("Examplary Sequence")

    str22 = "CTGCTGTTCCTTGCGATCGAAAAGATCAAGGGCGGACCGGTATCCGAGCGGGTTCAAGACTTTTGTTATCGCATTGGCTCG"
    if st.button('Sequence'):
        st.write(str22)
