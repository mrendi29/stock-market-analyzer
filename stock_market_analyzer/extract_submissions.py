from pmaw import PushshiftAPI
import datetime as dt
import csv

FIELDS = ["created_utc", "id", "title", "selftext", "stickied"]

# Using pushift for now.
papi = PushshiftAPI()

after = int(dt.datetime(2021, 1, 6, 0, 0, 0).timestamp())
before = int(dt.datetime(2021, 7, 5, 0, 0, 0).timestamp())
results = papi.search_submissions(
    subreddit="wallstreetbets",
    after=after,
    before=before,
    filter=FIELDS,
    limit=500000,
)

csv.register_dialect(
    "submissions", delimiter=",", quoting=csv.QUOTE_MINIMAL, quotechar="|"
)
with open("submissions.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, FIELDS, restval="NULL", dialect="submissions")
    writer.writeheader()
    for submission in results:
        writer.writerow(submission)
