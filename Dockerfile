FROM python:3.6

RUN apt-get -qy update && apt-get -qy install python3-pip && pip3 install pipenv

#RUN mkdir app
VOLUME ["/app"]
WORKDIR /app
RUN ls

#COPY Pipfile .
#COPY Pipfile.lock .

RUN pip install pipenv
RUN pipenv install --system

COPY . .

RUN python3 setup.py install

ENTRYPOINT ["docker/entrypoint.sh"]

