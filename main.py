import pandas as pd
from datetime import datetime, timedelta
from tqdm import tqdm

from src.utils.playstore import get_reviews_for_date
from src.agents.extraction_agent import extract_topics_agent
from src.agents.merge_agent import merge_topics_agent
from src.agents.taxonomy_agent import normalize_topics
from src.agents.trend_agent import generate_trend

START = datetime(2024, 6, 1)
TODAY = datetime.now()

all_days = {}
current = START

while current <= TODAY:
    print(f"Processing: {current.date()}")
    reviews = get_reviews_for_date()

    extracted = extract_topics_agent(reviews)
    merged = merge_topics_agent(extracted)
    final = normalize_topics(merged)

    all_days[current.date()] = final

    current += timedelta(days=1)

report = generate_trend(all_days)
report.to_csv("output/sample_report_T.csv")
print("Report saved → output/sample_report_T.csv")
