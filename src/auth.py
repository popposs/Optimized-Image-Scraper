import os
import praw

reddit_client_id = os.environ['REDDIT_CLIENT_ID']
reddit_client_secret = os.environ['REDDIT_CLIENT_SECRET']
reddit_user_agent = os.environ['REDDIT_USER_AGENT']

def get_reddit():

    if 'REDDIT_CLIENT_ID' not in os.environ:
        print('Source REDDIT_CLIENT_ID')
        return None
    if 'REDDIT_CLIENT_SECRET' not in os.environ:
        print('Source REDDIT_CLIENT_SECRET')
        return None
    if 'REDDIT_USER_AGENT' not in os.environ:
        print('Source REDDIT_USER_AGENT')
        return None

    return praw.Reddit(client_id=reddit_client_id,
            client_secret=reddit_client_secret,
            user_agent=reddit_user_agent)


