FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD . /code/
WORKDIR /code
RUN pip install --no-cache-dir -r requirements/production.txt
RUN apt-get -q update
RUN apt-get -qy install httrack