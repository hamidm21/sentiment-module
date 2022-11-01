from datetime import datetime
from data._twitter import TwitterAPI
from preprocessing._twitter import cleaner
from models._polarity import polarity_blob
from models._huggingface import roberta_pol
from serpapi import GoogleSearch

class Sentiment:
    def __init__(self) -> None:
        pass

    def get_sentiment(self, ticker: str, from_t: datetime, num: int, ):
        tweets = TwitterAPI.fetch_by_content(ticker, num, from_t)
        clean = cleaner(tweets)
        sent = roberta_pol(clean)
        return sent

    def get_trend():
        params = {
        "device": "desktop",
        "engine": "google_trends",
        "q": "bitcoin",
        "data_type": "TIMESERIES",
        "tz": "0",
        "cat": "1086",
        "api_key": "secret_api_key"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

