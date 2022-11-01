import pandas as pd
from pandas_profiling import ProfileReport

def Profile(raw:pd.DataFrame):
    report = ProfileReport(raw)
    return report