### Optimized Image Scraper [WIP]

- Flask backend served with Nginx + Gunicorn
- React + jQuery frontend
- PostgreSQL for storing image metadata on filesystem
- Redis for caching
- Multithreaded image fetching
- Dockerized for ease of development
- ML compression (WIP)

Installation:
- create a `.env` from `sample.env`
- `pipenv shell`
- `make all`
- navigate to http://localhost:5000
