import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(layout='wide')
df_haar = pd.read_csv('processing_time_statistic.csv')
df_facebox = pd.read_csv('facebox_statistic.csv')

st.title('Faceid Statistic')
col0_0, col0_1 = st.beta_columns(2)
labels = ['load_body_time', 'str2img_time', 'detection_time',
        'img2str_time', 'create_message_time', 'send_time']
df_haar['total'] = 0
df_facebox['total'] = 0
for el in labels:
    df_haar['total'] += df_haar[el]
    df_facebox['total'] += df_facebox[el]
with col0_0:
    st.write('### Haar')
    st.write(df_haar)
with col0_1:
    st.write('### Facebox')
    st.write(df_facebox)
labels.append('total')
col1_0, col1_1 = st.beta_columns(2)
selections = {}
with col1_0:
    st.write('### Select params')
    for label in labels:
        selections[label] = st.checkbox(label)
with col1_1:
    st.write('### Mean Metric')
    dt = []
    for label in labels:
        dt.append([label, df_haar[label].mean(), df_facebox[label].mean()])
    metric = pd.DataFrame(dt, columns=['label', 'haar', 'facebox'])
    st.write(metric)
    st.write('No of processed Frames in a second ***with Haar***:', 1//df_haar['total'].mean())
    st.write('No of processed Frames in a second ***with Facebox***:', 1//df_facebox['total'].mean())
st.write('### Haar')
st.line_chart(df_haar[[el for el in selections if selections[el]]])
st.write('### Facebox')
st.line_chart(df_facebox [[el for el in selections if selections[el]]])
