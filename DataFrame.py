
# --- CARICAMENTO PACCHETTI --- #

import pandas as pd
import streamlit as st
# import numpy as np

# @st.cache_data
# def load_data():
#     return pd.read_excel(uploaded_file, engine="openpyxl", sheet_name="RIEPILOGO_FATTURATO")
# edited_df = st.experimental_data_editor(load_data(),num_rows="dynamic", key="data_editor"


def undo ():
    for key in st.session_state.keys():
        del st.session_state[key]

if "df" not in st.session_state:
        st.session_state["df"] = True

if "edited_df" not in st.session_state:
        st.session_state["edited_df"] = True
        
uploaded_file = st.sidebar.file_uploader("Scegli il tuo file Excel", type=("xlsx"))

if uploaded_file is not None:
   st.session_state.df = pd.read_excel(uploaded_file, engine="openpyxl", sheet_name="RIEPILOGO_FATTURATO")
   st.session_state.edited_df = st.experimental_data_editor(st.session_state.df, num_rows="dynamic",key="data_editor")
   button = st.button("Annulla Modifiche", key="Annulla", on_click=undo)
   st.session_state




# if button:
#    del st.session_state[edited_df]
        
#--- SESSION STATE ---#

# if "data_editor" not in st.session_state:
#     st.session_state["data_editor"]
# st.write("Here's the session state:")
# st.write(st.session_state["data_editor"])
# for the_key in st.session_state.keys():
#     st.write(the_key)
# for item in st.session_state.values():
#     item
# for key in st.session_state.key():
#     del st.session_state[key]
