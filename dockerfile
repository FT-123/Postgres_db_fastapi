FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/ww1

RUN pip install pipenv
COPY Pipfile Pipfile.lock /usr/src/ww1
RUN pip install psycopg2-binary
RUN pipenv install --system --dev

COPY . /usr/src/ww1

EXPOSE 8000