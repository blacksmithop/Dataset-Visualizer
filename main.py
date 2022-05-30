from numpy import kaiser
import streamlit as st
import pandas as pd
from os import listdir, path
from resources.findings.findingToJson import createJSON, combineJSON
from time import sleep

# from json import dump, load

st.title("Dashboard")

st.subheader("Visualizer")

df = pd.read_csv("./resources/csv/sanitized.csv")

jsonPath = "./resources/findings/"

# save last state
# def loadSaveState(_data=None, _mode="r+"):
#     with open(path.join(jsonPath, "restore.json"), _mode) as state:
#         if not _data:
#             last_choice = load(state)
#             print("You stoppd at:", last_choice)
#         else:
#             dump(_data, state, indent=4)
#             last_choice = _data
#         return last_choice


# last_state = loadSaveState()

# list of subjects
subjects = df.Subject.unique()

excluded_subjects = []

# sidebar elements

# filter by subject
st.sidebar.header("Filter")
subject_choice = st.sidebar.selectbox("Subject:", subjects)

# last_state["subject"] = subject_choice
# loadSaveState(_data=last_state, _mode="w")

# if choice := last_state["subject"]:
#     subject_choice = choice

subject = df["Subject"] = subject_choice


# view json file
files = listdir(path.join(jsonPath, "json"))
file_choice = st.sidebar.selectbox("Data:", files)


def viewFile(_path, _file):
    # if _file != "full-data.json":
    #     last_state["file"] = _file
    #     loadSaveState(_data=last_state, _mode="w")

    with open(path.join(_path, _file)) as fp:
        return fp.read()


# if choice := last_state["file"]:
#     if choice != "full-data.json":
#         file_choice = choice

st.sidebar.json(viewFile(path.join(jsonPath, "json"), file_choice))

file_name = st.sidebar.text_input(label="New file", key="file_name")

save_file = st.sidebar.button(label="Create")
compile_file = st.sidebar.button(label="Compile")


if save_file:
    with st.spinner("Creating file.."):
        sleep(1)
    createJSON(fileName=file_name)

if compile_file:
    with st.spinner("Writing to file.."):
        sleep(2)
    combineJSON()

# pass the dataframe
final_df = df[["Subject", "Journal Abstract Text"]]

st.dataframe(final_df, 500, 500)

with st.expander("Full data"):
    st.json(viewFile("./resources/findings/", "full-data.json"))
