import pandas as pd

# Only way to extract needed fields from 4gb csv file in order to work collaboratively.
with pd.read_csv(
    "wallstreetbets_comments.csv",
    usecols=["created_utc", "id", "link_id", "body", "score"],
    chunksize=250000,
) as reader:
    for chunk in reader:
        with open("comments.csv", "a", newline="") as f:
            chunk.to_csv(
                f,
                mode="a",
                sep="|",
                header=f.tell() == 0,
                index=False,
                line_terminator="\r\n",
            )
