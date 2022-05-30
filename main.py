import streamlit as st
import pandas as pd
from os import listdir, path
from resources.findings.findingToJson import createJSON, combineJSON
from time import sleep

# from json import dump, load

st.title("Dashboard")

st.subheader("Visualizer")

df = pd.read_csv("./resources/csv/plato_sanitized.csv")

jsonPath = "./resources/findings/"


# list of subjects
subjects = df.Subject.unique()

excluded_subjects = []

# sidebar elements

# filter by subject
st.sidebar.header("Filter")
subject_choice = st.sidebar.selectbox("Subject:", subjects)


subject = df["Subject"] = subject_choice


# view json file
files = listdir(path.join(jsonPath, "json"))
file_choice = st.sidebar.selectbox("Data:", files)


def viewFile(_path, _file):
    with open(path.join(_path, _file)) as fp:
        return fp.read()


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
    st.sidebar.error("Filename must be a subject")

if compile_file:
    with st.spinner("Writing to file.."):
        sleep(2)
    combineJSON()

# pass the dataframe
final_df = df[["Subject", "Journal Abstract Text"]]


# pagination
N = 15
page_num = 0
page_last = len(final_df) // N

col1, col2, col3 = st.columns(3)
with col1:
    st.button(label="<")
with col2:
    st.text(page_num)
with col3:
    st.button(label=">")


st.dataframe(data=final_df, width=500, height=500)

with st.expander(f"Compiled data ({len(files)})"):
    st.json(viewFile("./resources/findings/", "full-data.json"), expanded=False)
