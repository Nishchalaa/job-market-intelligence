import requests
import pandas as pd
from datetime import datetime

APP_ID = "your_app_id"
APP_KEY = "your_app_key"

def scrape_adzuna():
    searches = ["data engineer", "data analyst", "software engineer", "python developer"]
    data = []

    for query in searches:
        url = f"https://api.adzuna.com/v1/api/jobs/us/search/1"
        params = {
            "app_id": '4658c9f7',
            "app_key": '68ccdf7eebb0798edf2a5d2b684aadc7',
            "what": query,
            "results_per_page": 50,
            "content-type": "application/json"
        }
        response = requests.get(url, params=params)
        jobs = response.json().get("results", [])

        for job in jobs:
            data.append({
                "title": job.get("title", ""),
                "company": job.get("company", {}).get("display_name", ""),
                "location": job.get("location", {}).get("display_name", ""),
                "description": job.get("description", ""),
                "salary": str(job.get("salary_min", "")),
                "category": query,
                "source": "adzuna",
                "scraped_at": datetime.today().strftime("%Y-%m-%d")
            })

    print(f"Adzuna: scraped {len(data)} jobs")
    return pd.DataFrame(data)