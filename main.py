import pandas as pd
from datetime import datetime, timedelta
from tqdm import tqdm

from src.agents.ingestion_agent import ingestion_agent
from src.agents.extraction_agent import extract_topics_agent
from src.agents.merge_agent import merge_topics_agent
from src.agents.taxonomy_agent import normalize_topics
from src.agents.trend_agent import generate_trend

START = datetime(2024, 6, 1)
TODAY = datetime.now()

all_days = {}
current = START

while current <= TODAY:
    print(f"\n[PROCESSING] {current.date()}")
    
    reviews = ingestion_agent(current.date())
    if not reviews:
        print("No reviews extracted.")
        current += timedelta(days=1)
        continue

    extracted = extract_topics_agent(reviews)
    merged = merge_topics_agent(extracted)
    final_topics = normalize_topics(merged)

    all_days[current.date()] = final_topics

    current += timedelta(days=1)

print("\n[INFO] Generating Trend Report (T-30 → T)...")
report = generate_trend(all_days)
report.to_csv("output/sample_report.csv")

print("\n Trend report saved at: output/sample_report.csv")
