import streamlit as st
import pandas as pd

# Load the Excel file
df = pd.read_excel("Engagement_Catalog_Phase_for_Agent.xlsx", engine="openpyxl")

# Clean column names
df.columns = [col.strip() for col in df.columns]

# Allowed Customer Impact Metrics   
allowed_metrics = [
    "Acquisition Rate", "ARPU", "Churn Rate", "First Call Resolution", "Call-in Rate",
    "Truck Roll Rate", "Cost of Acquisition", "Time to Value", "Take Rate", "NPS",
    "Trouble Ticket 1st 45 days"
]

# App title
st.title("Engagement Catalog Explorer")

# Sidebar filters
st.sidebar.header("Filter Engagements")
selected_product = st.sidebar.selectbox("Select engagements for Product", [""] + sorted(df["Product"].dropna().unique()))
selected_metric = st.sidebar.selectbox("Select engagements with a Customer Impact Metric", [""] + allowed_metrics)

# Show allowed metrics
if st.sidebar.button("Show available Customer Impact Metrics"):
    st.write("### Allowed Customer Impact Metrics")
    for metric in allowed_metrics:
        st.write(f"- {metric}")

# Filter logic
filtered_df = df.copy()
if selected_product:
    filtered_df = filtered_df[filtered_df["Product"] == selected_product]
if selected_metric:
    filtered_df = filtered_df[filtered_df["Customer Impact Metrics"].str.contains(selected_metric, na=False)]

# Display results
st.write("### Engagements Matching Your Criteria")
if not filtered_df.empty:
    for _, row in filtered_df.iterrows():
        st.write(f"**New Engagement Name:** {row['New Engagement Name']}")
        st.write(f"**Product:** {row['Product']}")
        st.write(f"**Headline:** {row['Headline']}")
        st.write(f"**Description:** {row['Description']}")
        st.write(f"**Customer Impact Metrics:** {row['Customer Impact Metrics']}")
        st.write(f"**Measures of Success:** {row['Measures of Success']}")
        st.markdown("---")
else:
    st.write("No engagements found matching the selected criteria.")
