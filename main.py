import streamlit as st
import pandas as pd
import numpy as np
from os import listdir
from resources.findings.findingToJson import createJSON, combineJSON
from time import sleep
from utils.file import viewFile

st.title("Dashboard")
st.subheader("Visualizer")

# dataset
xls = pd.ExcelFile("./resources/xlsx/output.xlsx")
df = pd.read_excel(xls)

# path to json files
jsonPath = "./resources/findings/"


# list of subjects
subjects = df.Subject.unique()
subjects = sorted(subjects)
excluded_subjects = []

# sidebar

# filter by subject
st.sidebar.header("Filter")
subject_choice = st.sidebar.selectbox("Subject:", subjects)


# display the Dataframe
df.loc[df.Subject == subject_choice]

# view json file
files = listdir(path.join(jsonPath, "json"))
file_choice = st.sidebar.selectbox("Data:", files)


st.sidebar.json(viewFile(path.join(jsonPath, "json"), file_choice), expanded=False)

file_name = st.sidebar.text_input(label="New file", key="file_name")

side_col1, side_col2 = st.columns(2)

with side_col1:
    save_file = st.sidebar.button(label="Create")
with side_col2:
    compile_file = st.sidebar.button(label="Compile")


if save_file:
    if file_name in subjects:
        with st.spinner("Creating file.."):
            sleep(1)
            createJSON(fileName=file_name)
            st.sidebar.success("File created")
    else:
        st.sidebar.error("Filename must be a subject")

if compile_file:
    with st.spinner("Writing to file.."):
        sleep(2)
    combineJSON()
    st.sidebar.success("Compiled file")


with st.expander(f"Compiled data ({len(files)})"):
    st.json(viewFile("./resources/findings/", "full-data.json"), expanded=False)
