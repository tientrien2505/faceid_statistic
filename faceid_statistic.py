import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(layout='wide')
df_haar = pd.read_csv('processing_time_statistic.csv')
df_facebox = pd.read_csv('facebox_statistic.csv')
df_facebox_encode = pd.read_csv('facebox_encode_statistic.csv')
df_facebox_fullencode = pd.read_csv('facebox_fullencode_statistic.csv')
df_haar_fullencode = pd.read_csv('haar_fullencode_statistic.csv')
df_haar_2k_fullencode = pd.read_csv('haar_2k_fullencode_statistic.csv')
df_haar_2k_200x200_fullencode = pd.read_csv('haar_2k_200x200_fullencode_statistic.csv')

st.title('Faceid Statistic')
col0_0, col0_1, col0_2, col0_3, col0_4, col0_5, col0_6 = st.columns(7)
labels = ['load_body_time', 'str2img_time', 'detection_time',
        'img2str_time', 'create_message_time', 'send_time']
df_haar['total'] = 0
df_facebox['total'] = 0
df_facebox_encode['total'] = 0
df_facebox_fullencode['total'] = 0
df_haar_fullencode['total'] = 0
df_haar_2k_fullencode['total'] = 0
df_haar_2k_200x200_fullencode['total'] = 0
for el in labels:
    df_haar['total'] += df_haar[el]
    df_facebox['total'] += df_facebox[el]
    df_facebox_encode['total'] += df_facebox_encode[el]
    df_facebox_fullencode['total'] += df_facebox_fullencode[el]
    df_haar_fullencode['total'] += df_haar_fullencode[el]
    df_haar_2k_fullencode['total'] += df_haar_2k_fullencode[el]
    df_haar_2k_200x200_fullencode['total'] += df_haar_2k_200x200_fullencode[el]
with col0_0:
    st.write('### Haar')
    st.write(df_haar)
with col0_1:
    st.write('### Facebox')
    st.write(df_facebox)
with col0_2:
    st.write('### Facebox Encode')
    st.write(df_facebox_encode)
with col0_3:
    st.write('### Facebox Full Encode')
    st.write(df_facebox_fullencode)
with col0_4:
    st.write('### Haar Full Encode')
    st.write(df_haar_fullencode)
with col0_5:
    st.write('### Haar 2k Full Encode')
    st.write(df_haar_2k_fullencode)
with col0_6:
    st.write('### Haar 2k 200x200 Full Encode')
    st.write(df_haar_2k_200x200_fullencode)
labels.append('total')
col1_0, col1_1 = st.columns((1, 2))
selections = {}
with col1_0:
    st.write('### Select params')
    for label in labels:
        selections[label] = st.checkbox(label)
with col1_1:
    st.write('### Mean Metric')
    dt = []
    for label in labels:
        dt.append([label, df_haar[label].mean(), df_facebox[label].mean(), df_facebox_encode[label].mean(), df_facebox_fullencode[label].mean(), df_haar_fullencode[label].mean()
        , df_haar_2k_fullencode[label].mean(), df_haar_2k_200x200_fullencode[label].mean()])
    metric = pd.DataFrame(dt, columns=['label', 'haar', 'facebox', 'facebox_encode', 'facebox_fullencode', 'haar_fullencode'
    , 'haar_2k_fullencode', 'haar_2k_200x200_fullencode'])
    st.write(metric)
    st.write('No of processed Frames in a second ***with Haar***:', 1//df_haar['total'].mean())
    st.write('No of processed Frames in a second ***with Facebox***:', 1//df_facebox['total'].mean())
    st.write('No of processed Frames in a second ***with Facebox Encode***:', 1//df_facebox_encode['total'].mean())
    st.write('No of processed Frames in a second ***with Facebox Full Encode***:', 1//df_facebox_fullencode['total'].mean())
    st.write('No of processed Frames in a second ***with Haar Full Encode***:', 1//df_haar_fullencode['total'].mean())
    st.write('No of processed Frames in a second ***with Haar 2k Full Encode***:', 1//df_haar_2k_fullencode['total'].mean())
    st.write('No of processed Frames in a second ***with Haar 2k 200x200 Full Encode***:', 1//df_haar_2k_200x200_fullencode['total'].mean())
st.write('### Haar')
st.line_chart(df_haar[[el for el in selections if selections[el]]])
st.write('### Facebox')
st.line_chart(df_facebox [[el for el in selections if selections[el]]])
st.write('### Facebox Encode')
st.line_chart(df_facebox_encode [[el for el in selections if selections[el]]])
st.write('### Facebox Full Encode')
st.line_chart(df_facebox_fullencode [[el for el in selections if selections[el]]])
st.write('### Haar Full Encode')
st.line_chart(df_haar_fullencode [[el for el in selections if selections[el]]])
st.write('### Haar 2k Full Encode')
st.line_chart(df_haar_2k_fullencode [[el for el in selections if selections[el]]])
st.write('### Haar 2k 200x200 Full Encode')
st.line_chart(df_haar_2k_200x200_fullencode [[el for el in selections if selections[el]]])
