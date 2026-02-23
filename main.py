from scrapers.remotive import scrape_remotive
from scrapers.adzuna import scrape_adzuna
from pipeline.cleaner import clean_df
import sqlite3
import pandas as pd

def save_to_db(df):
    conn = sqlite3.connect("database/jobs.db")
    df.to_sql("jobs", conn, if_exists="append", index=False)
    conn.close()
    print(f"Saved {len(df)} jobs to database")

if __name__ == "__main__":
    df1 = scrape_remotive()
    df2 = scrape_adzuna()
    
    df = pd.concat([df1, df2], ignore_index=True)
    df = clean_df(df)
    save_to_db(df)
    print("Done!")