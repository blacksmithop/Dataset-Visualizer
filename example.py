import streamlit as st
import pandas as pd
from os import listdir, path
from json import loads

st.title("Example")

st.subheader("Visualizer")

df = pd.read_csv("./data/us-500.csv")

# list of companys
companys = df.company_name.unique()

excluded_companys = []

# sidebar elements

st.sidebar.header("Filter")
make_choice = st.sidebar.selectbox("Options:", companys)
company = df["company_name"] = make_choice


# list of files
jsonPath = "./data/colors/"
files = listdir(jsonPath)
file_choice = st.sidebar.selectbox("Data:", files)


def viewFile(fileName):
    with open(path.join(jsonPath, file_choice)) as fp:
        return fp.read()


st.sidebar.json(viewFile(file_choice))

# pass the dataframe
final_df = df[["first_name", "company_name"]]

st.dataframe(final_df, 500, 500)
