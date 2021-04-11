import streamlit as st
import pandas as pd
import io
import os
import base64

def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  
    href = f'<a target="_blank" href="data:file/csv;base64,{b64}">Download csv file</a>'
    return (href)
    
# filename = file_selector()
filename = st.file_uploader("Choose SAS file", type=["sas7bdat"])

if (filename is not None):
    st.write('You selected `%s`' % filename.name)
    df = pd.read_sas (filename, format = 'sas7bdat')
    st.write(df)
    href = get_table_download_link(df)
    st.markdown(href, unsafe_allow_html=True)

