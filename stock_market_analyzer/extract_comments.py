from pmaw import PushshiftAPI
import datetime as dt
import csv

csv.register_dialect(
    "submissions", delimiter=",", quoting=csv.QUOTE_MINIMAL, quotechar="|"
)
FIELDS = ["created_utc", "id", "link_id", "body", "score"]

papi = PushshiftAPI()

comments_for_month = int(50 / 7)

# We want first 7 months
for i in range(1, 7):
    after = int(dt.datetime(2021, i, 6, 0, 0, 0).timestamp())
    before = int(dt.datetime(2021, i + 1, 5, 0, 0, 0).timestamp())
    results = papi.search_comments(
        subreddit="wallstreetbets",
        after=after,
        before=before,
        filter=FIELDS,
        limit=comments_for_month,
    )

    with open("comments.csv", "w") as f:
        writer = csv.DictWriter(f, FIELDS, restval="NULL", dialect="submissions")
        writer.writeheader()
        for submission in results:
            writer.writerow(submission)
