from datetime import datetime
from src.data._twitter import TwitterAPI
from src.preprocessing._twitter import cleaner
from src.models._polarity import polarity_blob
from src.models._huggingface import roberta_pol
from src.data._google import google_trend


class Sentiment:
    def __init__(self) -> None:
        pass

    def get_sentiment(
        self,
        ticker: str,
        from_t: datetime,
        num: int,
    ):
        tweets = TwitterAPI.fetch_by_content(ticker, num, from_t)
        clean = cleaner(tweets)
        sent = roberta_pol(clean)
        return sent

    def get_trend():
        return google_trend("bitcoin", "")
