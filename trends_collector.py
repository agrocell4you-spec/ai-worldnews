from pytrends.request import TrendReq

def get_trending_keywords(country, num):

    pytrend = TrendReq()

    df = pytrend.trending_searches(pn=country)

    keywords = df[0].tolist()

    return keywords[:num]