import sqlite3
import pandas as pd

conn = sqlite3.connect("database/jobs.db")
df = pd.read_sql("SELECT * FROM jobs", conn)
conn.close()

# most in demand skills
all_skills = df["skills"].dropna().str.split(", ")
from collections import Counter
skill_counts = Counter([skill for sublist in all_skills for skill in sublist])

print("\n🔥 Top 10 Most In Demand Skills:")
for skill, count in skill_counts.most_common(10):
    print(f"  {skill}: {count} jobs")

# most hiring companies
print("\n🏢 Top Hiring Companies:")
print(df["company"].value_counts().head(10))

# jobs by category
print("\n📂 Jobs by Category:")
print(df["category"].value_counts())

# jobs with salary listed
has_salary = df[df["salary"] != ""]
print(f"\n💰 Jobs with salary info: {len(has_salary)} out of {len(df)}")