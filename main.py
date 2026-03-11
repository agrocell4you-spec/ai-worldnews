from trends_collector import get_trending_keywords
from content_generator import generate_article
from blogger_poster import post_to_blogger
from pdf_report import make_pdf
from config.schedule_config import SCHEDULE
from datetime import datetime

def run():

    now=datetime.now().strftime("%H:%M")

    if now not in SCHEDULE:
        return

    jobs=SCHEDULE[now]

    posts=[]

    for job in jobs:

        keywords=get_trending_keywords(
            job["country"],
            job["keywords"]
        )

        for kw in keywords:

            article=generate_article(
                kw,
                job["language"]
            )

            title=kw

            post_to_blogger(title,article)

            posts.append((title,article))

    make_pdf(posts)

if __name__=="__main__":
    run()