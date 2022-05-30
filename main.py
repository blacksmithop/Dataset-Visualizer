import streamlit as st
import pandas as pd
from os import listdir, path
from json import loads

st.title("Dashboard")

st.subheader("Visualizer")

df = pd.read_csv("./data/sanitized.csv")

# list of subjects
subjects = df.Subject.unique()

excluded_subjects = []

# sidebar elements

st.sidebar.header("Filter")
make_choice = st.sidebar.selectbox("Subject:", subjects)
subject = df["Subject"] = make_choice

# filter by subject
btn_container = st.sidebar.container()

add_sub = btn_container.button("Add", help="Exclude the selected subject")
remove_sub = btn_container.button("Remove", help="Exclude the selected subject")

# list of files
jsonPath = "./data/json/"
files = listdir(jsonPath)
file_choice = st.sidebar.selectbox("Data:", files)


def viewFile(fileName):
    with open(path.join(jsonPath, file_choice)) as fp:
        return fp.read()


st.sidebar.json(viewFile(file_choice))

# pass the dataframe
final_df = df[["Subject", "Journal Abstract Text"]]

st.dataframe(final_df, 500, 500)
