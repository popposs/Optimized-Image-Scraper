### Cats of Reddit [WIP]

Scrape cats off reddit.
- Flask backend served with Nginx + Gunicorn (WIP)
- React + jQuery frontend
- PostgreSQL for storing image metadata on filesystem
- Redis for caching
- Multithreaded image fetching
- Dockerized for ease of development

Installation:
- `pipenv shell`
- `make all`
- navigate to http://localhost:5000
