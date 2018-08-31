all: stop-all build-all run-all
start-data: start-db start-cache

stop: stop-all

# stop docker containers
stop-all: stop-app stop-db stop-cache

stop-db:
	-docker stop docker_db_1

stop-cache:
	-docker stop docker_cache_1

stop-app:
	-docker stop docker_backend_1


# build and tag app
build-all:
	-pipenv run docker build -t 'backend' .

run-all:
	-docker-compose -f docker/docker-compose.yml up -d

# individually stop & start containers
db: stop-db start-db

cache: stop-cache start-cache

app: stop-app start-app

start-db:
	-docker-compose -f docker/docker-compose.yml up -d db

start-cache:
	-docker-compose -f docker/docker-compose.yml up -d cache

start-app:
	-docker-compose -f docker/docker-compose.yml up -d backend

