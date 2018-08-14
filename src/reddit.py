from auth import get_reddit
from channels import CHANNELS
from cache import cache_client


def check_cached(val):
	return val.decode('utf-8') if val else None

if __name__ == '__main__':
	reddit = get_reddit()

	try:
		for channel in CHANNELS:
			print(channel, '\n')
			for submission in reddit.subreddit(channel).hot(limit=10):
				url = cache_client.get(submission.title)
				cached = check_cached(url)
				if cached is None:
					cache_client.set(submission.title, submission.url.encode('utf-8'))
					print('\t', submission.url)
				else:
					print('Cached:\t', cached)

	except Exception as e:
		print('Exception:', e)

