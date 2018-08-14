from auth import get_reddit
from channels import CHANNELS
from cache import cache_client
import time

reddit = get_reddit()

def get_top_posts():
	global reddit
	posts = {}

	for channel in CHANNELS:
		urls = cache_client.get(channel)

		if urls is None:
			submissions = reddit.subreddit(channel).hot(limit=10)
			urls = [ s.url for s in submissions ]
			cache_client.set(channel, urls, ex=60) # cache for 1 minute

		posts[channel] = urls
	
	return posts

if __name__ == '__main__':
	print(get_top_posts())

