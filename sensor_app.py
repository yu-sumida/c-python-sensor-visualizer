import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Sensor Data Visualization(C X python)')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Sample:",df.head())

    #temprature graph
    st.subheader('Temperature Graph')
    plt.figure()
    plt.plot(df['time'], df['temperature'], label='temperature(℃)')
    plt.xlabel('time')
    plt.ylabel('temperature (℃)')
    plt.legend()
    st.pyplot(plt)

    #humidity graph
    st.subheader('Humidity Graph')
    plt.figure()
    plt.plot(df['time'], df['humidity'], label='humidity(%)', color='green')
    plt.xlabel('time')
    plt.ylabel('humidity (%)')
    plt.legend()
    st.pyplot(plt)

    #acceleration graph
    st.subheader('Acceleration Graph')
    plt.figure()
    plt.plot(df['time'], df['acceleration'], label='acceleration(m/s²)', color='red')
    plt.xlabel('time')
    plt.ylabel('acceleration (m/s²)')
    plt.legend()
    st.pyplot(plt)

