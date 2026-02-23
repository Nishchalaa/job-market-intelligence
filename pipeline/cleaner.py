import re
import pandas as pd

SKILLS = [
    "python", "sql", "javascript", "typescript", "react", "node",
    "aws", "docker", "kubernetes", "git", "linux", "postgres",
    "mongodb", "spark", "airflow", "tableau", "power bi", "excel",
    "machine learning", "deep learning", "tensorflow", "pytorch",
    "pandas", "numpy", "scikit-learn", "java", "scala", "rust",
    "azure", "gcp", "kafka", "dbt", "snowflake", "redshift",
    "fastapi", "django", "flask", "redis", "terraform", "ansible",
    "looker", "databricks", "hadoop", "elasticsearch", "graphql"
]

def clean_description(text):
    text = re.sub("<.*?>", "", text)      # remove HTML tags
    text = re.sub("\s+", " ", text)       # remove extra whitespace
    return text.strip()

def extract_skills(description):
    description = description.lower()
    found = [skill for skill in SKILLS if skill in description]
    return ", ".join(found)

def clean_df(df):
    df = df.copy()  # add this line
    df = df.drop_duplicates(subset=["title", "company"])
    df["description"] = df["description"].apply(clean_description)
    df["skills"] = df["description"].apply(extract_skills)
    return df