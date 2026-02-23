import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from collections import Counter

# load data
conn = sqlite3.connect("database/jobs.db")
df = pd.read_sql("SELECT * FROM jobs", conn)
conn.close()

st.title("🔥 Tech Job Market Intelligence")
st.markdown(f"**{len(df)} jobs** collected so far")

# sidebar filters
st.sidebar.header("Filters")
category = st.sidebar.multiselect("Category", df["category"].unique(), default=df["category"].unique())
df = df[df["category"].isin(category)]

# top skills chart
st.subheader("Top In-Demand Skills")
all_skills = df["skills"].dropna().str.split(", ")
skill_counts = Counter([s for sublist in all_skills for s in sublist if s != ""])
skills_df = pd.DataFrame(skill_counts.most_common(15), columns=["skill", "count"])
fig = px.bar(skills_df, x="count", y="skill", orientation="h", color="count", color_continuous_scale="reds")
st.plotly_chart(fig)

# jobs by category
st.subheader("Jobs by Category")
fig2 = px.pie(df, names="category")
st.plotly_chart(fig2)

# top hiring companies
st.subheader("Top Hiring Companies")
companies_df = df["company"].value_counts().head(10).reset_index()
companies_df.columns = ["company", "count"]
fig3 = px.bar(companies_df, x="company", y="count", color="count", color_continuous_scale="blues")
st.plotly_chart(fig3)

# raw data table
st.subheader("Raw Jobs Data")
st.dataframe(df[["title", "company", "location", "category", "salary", "skills", "scraped_at"]])
