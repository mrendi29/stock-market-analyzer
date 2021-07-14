# Rename your .env.test file with .env and then replace all the variables with your API config.

# Notes

We used: https://github.com/pushshift/api

API CALL TO pushift(pmaw) to get last 500000 submissions from 10jan to 24 mar.

# Submission: title, id ,created_at,selftext

for each submission get all comment ids: https://api.pushshift.io/reddit/submission/comment_ids/{base36 submission id}
then for each comment id get:

# Comment: body,comment_id, link_id, created_at

METHOD 2 might change later:

for comment in reddit.subreddit('wallstreetbets').stream.comments(skip_existing=True):
print(comment)

for submission in reddit.subreddit('wallstreetbets').stream.submissions(skip_existing=True):
print(submission)
