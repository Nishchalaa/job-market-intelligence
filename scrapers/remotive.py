import requests
import pandas as pd
from datetime import datetime

def scrape_remotive():
    categories = ["software-dev", "data", "devops", "product"]
    data = []

    for category in categories:
        response = requests.get(f"https://remotive.com/api/remote-jobs?category={category}")
        jobs = response.json()["jobs"]

        for job in jobs:
            data.append({
                "title": job["title"],
                "company": job["company_name"],
                "location": job["candidate_required_location"],
                "description": job["description"],
                "salary": job.get("salary", ""),
                "category": category,
                "source": "remotive",
                "scraped_at": datetime.today().strftime("%Y-%m-%d")
            })

    print(f"Remotive: scraped {len(data)} jobs")
    return pd.DataFrame(data)