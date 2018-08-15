from src.logic.auth import get_reddit
from src.logic.channels import CHANNELS
from src.logic.cache import cache_client
import time

reddit = get_reddit()

def check_is_image(url):
	ext = url[-4:]
	return ext == '.jpg' or ext == '.png'

def get_top_posts():
	global reddit
	posts = {}

	for channel in CHANNELS:
		urls = cache_client.get(channel)

		if urls is None:
			submissions = reddit.subreddit(channel).hot(limit=10)
			urls = [ s.url for s in submissions if check_is_image(s.url) ]
			cache_client.set(channel, urls, ex=60) # cache for 1 minute
		else:
			urls = [ url.replace('\'', '').strip() for url in urls[1:-1].split(',') ]

		posts[channel] = urls

	return posts
