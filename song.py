"""
Created on Tue Jan 25 21:25:21 2022
"""
import numpy as np
import plotly.express as px
import pandas as pd
import streamlit as st


song = pd.read_csv('/Users/iiiii/Desktop/Data_Science/s.csv')
song = song.dropna()
slcbx = st.sidebar.selectbox(
    'Select one of the following:',
    ('Start', 'Fast selective data display device (FSDDAED)')    
)


if slcbx == 'Start':
    st.title('The Song Dataset')
    st.subheader('Introduction')
    st.markdown('In this case study, I will analyse the popular songs that are all stored in song.csv')
    st.markdown('I will also analyse what factors that the most popular song has.')
    

if slcbx == 'Fast selective data display device (FSDDAED)':
    st.title('Fast selective data display and explainatory device (FSDDAED)')
    st.subheader('A little bit crazy but nice.')
    yo = st.selectbox(
            'Select one of the following:',
            ('Column Explaination', 'Data Display')
        )
    if yo == 'Column Explaination':
        yo1 = st.selectbox(
                'Select one of the following:',
                ('song_name', 'song_popularity')
            )
        if yo1 == ''
    if yo == 'Data Display':
        song