all: stop-all build-all run-all

stop: stop-all

# stop docker containers 
stop-all: stop-redis stop-app

stop-redis:
	-docker stop docker_redis_1

stop-app:
	-docker stop docker_backend_1


# build and tag app
build-all:
	-pipenv run docker build -t 'backend' .

run-all:
	-docker-compose -f docker/docker-compose.yml up -d

# individually stop & start containers
redis: stop-redis build-redis

app: stop-app build-app

build-redis:
	-docker-compose -f docker/docker-compose.yml up -d redis

build-app:
	-docker-compose -f docker/docker-compose.yml up -d backend
