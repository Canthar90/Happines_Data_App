import streamlit as st
import plotly.express as px
import pandas as pd




df = pd.read_csv("happy.csv")
st.set_page_config(
    page_title="Happiness data app",
    page_icon="😊"
)

st.title("In search for Happiness")

cols = df.columns
message ="This app allow you to create scatter plot from data about happiness\
    you can choose values for x and y axis. Available values"
message_add = [(column + ', ') for column in cols]
mess2 = ""
for mess in message_add:
    mess2 += mess
message =  message + mess2

st.info(message)

x_option = st.selectbox("Select data for X axis", (df.columns))

y_option = st.selectbox("Select data for Y axis", (df.columns))

st.subheader(f"{x_option} and {y_option}")
x = df[x_option]
y = df[y_option]  

plot = px.scatter(x=x, y=y, labels={"x": x_option, "y": y_option})

st.plotly_chart(plot)


st.info("Created by Dawid Cieślak")