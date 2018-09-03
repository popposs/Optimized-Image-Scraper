FROM python:3.6

RUN apt-get -qy update && apt-get -qy install python3-pip && pip3 install pipenv
RUN pip install pipenv

VOLUME ["/app"]
WORKDIR /app

COPY Pipfile* /tmp/

RUN cd /tmp && \
    pipenv install --system

COPY . .

RUN python3 setup.py install

ENTRYPOINT ["docker/entrypoint.sh"]

