from google_play_scraper import reviews, Sort

def get_reviews_for_date(package="in.swiggy.android", count=200):
    result, _ = reviews(
        package,
        lang="en",
        country="in",
        sort=Sort.NEWEST,
        count=count
    )
    return [r["content"] for r in result]
