FROM python:3.11.0-slim-buster

ENV APP_HOME=/app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

LABEL maintainer='example@email.com'
LABEL description="Development image for Instagram Influencers"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev \
    && apt-get install -y gettext \
    && apt-get install -y netcat gcc postgresql \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./docker/local/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

CMD ["uvicorn", "setup.main:app", "--host", "0.0.0.0", "--port", "8000"]

ENTRYPOINT [ "/entrypoint" ]