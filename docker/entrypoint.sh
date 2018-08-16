#!/bin/bash

echo "client id" $REDDIT_CLIENT_ID
echo "client secret" $REDDIT_CLIENT_SECRET
echo "user agent" $REDDIT_USER_AGENT

src/utils/wait-for-it -t 30 redis:6379

echo "Running backend!"
python3 src/app.py
