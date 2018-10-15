#!/bin/bash

src/utils/wait-for-it -t 10 cache:6379
src/utils/wait-for-it -t 10 db:5432

echo "Running backend!"
#python3 src/app.py
gunicorn app:app -w 4 -b :5090
#curl -i http://localhost:5000/
