all: stop build run

stop:
	-docker stop docker_redis_1
	-docker stop docker_backend_1

build:
	-pipenv run docker build -t 'backend' .

run:
	-docker-compose -f docker/docker-compose.yml up
