# Sensor Data Visualization Tool (C × Python × Streamlit)

> For Japanese, see [README_ja.md](./README_ja.md)

## Overview

This project simulates three types of sensor data—temperature, humidity, and acceleration—using C language,  
and outputs them as a CSV file.  
The data is then visualized with a Python web application built with Streamlit.  
This portfolio project showcases skills in both embedded development and data science.

---

## Features

- Generation of multiple types of sensor data (temperature, humidity, acceleration) using C
- Output data saved as a CSV file
- Data visualization (line graphs, etc.) using Python and Streamlit
- Easy reproducibility with a virtual environment and requirements.txt

---

## Usage

### 1. Generate the CSV file with C

Compile and run the C program:

```sh
gcc main.c -o main
./main
```
### 2. Set up a Python virtual environment and install libraries

```sh
python -m venv venv
venv\Scripts\activate (windows)
source venv/bin/activate (Mac/Linux)
```
Install required libraries:
```sh
pip install -r requirements.txt
```
### 3. Run the Streamlit app
```sh
streamlit run sensor_app.py
```