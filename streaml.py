import streamlit as st
import pandas as pd
import io
import os
import base64
from pathlib import Path

def get_table_download_link(df, out_name):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  
    href = f'<a target="out.csv" download={out_name} href="data:file/csv;base64,{b64}">Download {out_name} file</a>'
    return (href)
    
# filename = file_selector()
filename = st.file_uploader("Choose SAS file", type=["sas7bdat"])

if (filename is not None):
    st.write('You selected `%s`' % filename.name)
    df = pd.read_sas (filename, format = 'sas7bdat')
    st.write(df)
    filename_stem = Path(filename.name).stem + ".csv"
    st.write('Output file: `%s`' % filename_stem)
    href = get_table_download_link(df, filename_stem)
    st.markdown(href, unsafe_allow_html=True)

