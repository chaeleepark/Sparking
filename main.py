import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
patients = [
    {"Name": "Alice Kim", "Visits": 3},
    {"Name": "Brian Lee", "Visits": 5},
    {"Name": "Carlos Rivera", "Visits": 2},
    {"Name": "Dana Patel", "Visits": 4}
]

df = pd.DataFrame(patients)

# Streamlit app layout
st.set_page_config(page_title="Healthcare Dashboard", layout="centered")
st.title("🩺 Healthcare Dashboard")

# Display patient list
st.subheader("Patient List")
st.dataframe(df, use_container_width=True)

# Display bar chart
st.subheader("Visits per Patient")
fig = px.bar(df, x="Name", y="Visits", color="Name", title="Patient Visits", height=400)
st.plotly_chart(fig, use_container_width=True)
