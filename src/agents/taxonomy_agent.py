def normalize_topics(merged_topics):
    cleaned = {}
    for k, v in merged_topics.items():
        text = v.lower()
        if "rude" in text or "impolite" in text:
            cleaned[k] = "delivery partner rude"
        elif "delay" in text or "late" in text:
            cleaned[k] = "delivery issue"
        elif "stale" in text or "bad" in text:
            cleaned[k] = "food stale"
        else:
            cleaned[k] = v
    return cleaned
