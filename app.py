import streamlit as st
import pandas as pd

st.title("Streamlit Mini-project App")
st.header("Student Data Analysis App")
st.text("Welcome to my firs streamlit app")

df = pd.read_csv("student_score.csv")

st.subheader("Dataset Preview")
if st.button("Show Dataset"):
    st.dataframe(df)

st.subheader("Dataset Summary")
st.write(df.describe())

st.subheader("Data selector")
min_Total_score = st.slider("Select Minimum Total_score", 0, 100, 50)
filtered_df = df[df["Total_score"] >= min_Total_score]
st.dataframe(filtered_df)

st.subheader("File uploads")
uploaded_file = st.file_uploader("Upload CSV file")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.subheader("Data Visualization")
st.write("LINE CHART")
st.line_chart(df, x = "Study_hour", y = "Total_score")
st.write("SCATTER CHART")
st.scatter_chart(df, x = "Study_hour", y = "Total_score")
st.write("BAR CHART")
st.bar_chart(df, x = "Study_hour", y = "Total_score")


import matplotlib.pyplot as plt

st.write("HISTOGRAM")
fig, ax = plt.subplots()
ax.hist(df["Total_score"])
ax.set_xlabel("Total_score")
ax.set_ylabel("freuency")
ax.set_title("Distribution of score")
st.pyplot(fig)


st.subheader("Navigation show")
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose View",
    ["Dataset Preview", "Data Set Summary", "Data Selector", "File uploads", "Data Visualizations"]
)




if option == "Dataset Preview":
    st.dataframe(df)

elif option == "Data Set Summary":
    st.write(df.describe())

elif option == "Data Selector":
      st.dataframe(filtered_df)

elif option == "File uploads":
     
           st.dataframe(df)

elif option == "Visualizations":
    st.bar_chart(df["department"].value_counts())
