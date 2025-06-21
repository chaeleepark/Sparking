import streamlit as st
import pandas as pd
import plotly.express as px

# App config
st.set_page_config(page_title="WISDOM Trial Dashboard", layout="centered")
st.title("🎗️ WISDOM Trial Dashboard – Laura Esserman's Legacy")

st.write("""
Dr. Laura Esserman's WISDOM Trial is revolutionizing how breast cancer is screened and treated. This landmark study tests whether **personalized screening** — based on genetic and risk factors — can safely replace one-size-fits-all annual mammography.
""")

# Simulated outcome data
data = pd.DataFrame({
    "Screening Strategy": ["Annual Mammogram", "Personalized Screening"],
    "Biopsies per 1000 Women": [75, 40],
    "Cancers Detected": [6.5, 6.3],
    "Overdiagnosed Cases": [2.1, 0.8],
    "Anxiety Reported (%)": [28, 17]
})

st.subheader("📋 Simulated Outcomes by Screening Strategy")
st.dataframe(data, use_container_width=True)

# Plot: Biopsies and Overdiagnosis
st.subheader("📉 Reduced Harm with Personalized Screening")

harm_df = data[["Screening Strategy", "Biopsies per 1000 Women", "Overdiagnosed Cases"]].melt(
    id_vars="Screening Strategy", var_name="Metric", value_name="Value"
)

fig = px.bar(harm_df, x="Metric", y="Value", color="Screening Strategy",
             barmode="group", title="Fewer Biopsies and Overdiagnosis with Personalized Screening",
             labels={"Value": "Cases per 1000 Women"})
fig.update_layout(height=400)
st.plotly_chart(fig, use_container_width=True)

# Highlight impact
st.success("WISDOM is helping reshape breast cancer care by focusing on what matters: risk, genetics, and avoiding unnecessary harm.")

st.caption("Note: All data above is simulated and illustrative. For real findings, see wisdomstudy.org or UCSF publications.")
