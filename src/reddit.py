from auth import get_reddit

reddit = get_reddit()

print(reddit.read_only)

for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)
