import streamlit as st
import pandas as pd
import plotly.express as px

# Title and description
st.set_page_config(page_title="DCIS Dashboard", layout="centered")
st.title("🩺 DCIS Management Dashboard – Inspired by Dr. Laura Esserman’s Work")
st.write("""
This app highlights trends in the management of Ductal Carcinoma In Situ (DCIS), inspired by research led by Dr. Laura Esserman at UCSF. 
Her work promotes precision medicine and reducing overtreatment through active surveillance, particularly in early-stage breast cancers.
""")

# Sample data
data = pd.DataFrame({
    "Patient Group": ["Active Surveillance", "Surgery + Radiation", "Hormone Therapy"],
    "5-Year Progression (%)": [6, 2, 4],
    "Avg Age": [58, 55, 59]
})

# Show data
st.subheader("Management Strategies for DCIS Patients")
st.dataframe(data, use_container_width=True)

# Plot
st.subheader("5-Year Progression Risk by Management Strategy")
fig = px.bar(data, x="Patient Group", y="5-Year Progression (%)", 
             color="Patient Group", text="5-Year Progression (%)",
             labels={"5-Year Progression (%)": "Progression Risk (%)"},
             title="Comparing DCIS Management Approaches")
fig.update_traces(textposition='outside')
st.plotly_chart(fig, use_container_width=True)

# Note
st.info("Note: This data is illustrative and simplified. Real trial outcomes may vary (e.g., WISDOM, COMET).")
