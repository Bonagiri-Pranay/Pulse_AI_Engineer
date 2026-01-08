import pandas as pd
from collections import Counter
from datetime import timedelta

def generate_trend(all_days, window=30):
    all_topics = set()

    for date, topics in all_days.items():
        all_topics.update(topics.values())

    dates = sorted(all_days.keys())
    T = dates[-1]
    date_range = [T - timedelta(days=i) for i in range(window)][::-1]

    data = {topic: [] for topic in all_topics}

    for d in date_range:
        day_topics = all_days.get(d, {})
        counts = Counter(day_topics.values())

        for topic in all_topics:
            data[topic].append(counts.get(topic, 0))

    df = pd.DataFrame(data, index=date_range).T
    return df
