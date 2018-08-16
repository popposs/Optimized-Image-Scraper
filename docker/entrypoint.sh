#!/bin/bash

src/utils/wait-for-it -t 30 redis:6379

echo "Running backend!"
python3 src/app.py
curl -i http://localhost:5000/
