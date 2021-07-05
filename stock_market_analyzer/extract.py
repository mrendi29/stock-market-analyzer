import praw
import os
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("client_id"),
    client_secret=os.getenv("client_secret"),
    username=os.getenv("username"),
    password=os.getenv("password"),
    user_agent=os.getenv("user_agent"),
)
reddit.read_only = True
subreddit = reddit.subreddit("wallstreetbets")
hot = subreddit.hot(limit=10)

counttotal = 0  # total number of comment read
submissions_counter = 0

# Submission: Likely neeed submission title, id ,created_at
# Comment: body, link_id, created_at

for submissions in hot:
    if not submissions.stickied:
        submissions_counter += 1
        # These are usually the pinned posts(rules, etc)
        if submissions_counter > 5:
            submissions.comments.replace_more(limit=None)
            comments = submissions.comments.list()
            for comment in comments:
                if isinstance(comment, MoreComments):
                    continue
                print(comment.body)
                counttotal += 1

print(counttotal)
print(submissions_counter)
