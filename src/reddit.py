from auth import get_reddit
from channels import CHANNELS
from cache import cache_client
import time


def check_cached(val):
	return val.decode('utf-8') if val else None

if __name__ == '__main__':
	reddit = get_reddit()
	start = time.time()


	for channel in CHANNELS:
		print(channel, '\n')
		urls = cache_client.get(channel)
		cached = check_cached(urls)

		if cached is None:
			submissions = reddit.subreddit(channel).hot(limit=10)
			urls = [ s.url for s in submissions ]
			cache_client.set(channel, urls, ex=60) # cache for 1 minute

		print('\t', urls)

	end = time.time()
	print(end - start)
