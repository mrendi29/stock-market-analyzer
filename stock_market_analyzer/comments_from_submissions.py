import pandas as pd
import csv
import requests


def get_comments_for_submission(id):
    result = requests.get(
        f"https://api.pushshift.io/reddit/submission/comment_ids/{id}"
    )
    if result.status_code == 200:
        return ",".join(result.json().get("data"))
    return []


submissions = pd.read_csv(
    "submissions.csv", delimiter=",", quoting=csv.QUOTE_MINIMAL, quotechar="|"
)
submissions.selftext = submissions.selftext.str.replace("\n+", "\\n", regex=True)

print(submissions.head())

submissions["comment_ids"] = submissions["id"].apply(
    lambda id: get_comments_for_submission(id)
)

submissiprint(submissions.head())

submissions.to_csv(
    "submissions-formatted.csv",
    sep=",",
    quoting=csv.QUOTE_MINIMAL,
    quotechar="|",
    index=False,
)
