from src.utils.playstore import get_reviews_for_date

def ingestion_agent(date):
    """
    Ingestion Agent
    ----------------
    Fetches Google Play Store reviews for a given date.
    The assignment says: treat each day's reviews as a batch.

    Parameters:
        date (datetime.date): The day for which reviews must be fetched.

    Returns:
        list[str]: A list of review text strings.
    """
    try:
        reviews = get_reviews_for_date()
        return reviews
    except Exception as e:
        print(f"[ERROR] Failed to fetch reviews for {date}: {e}")
        return []
