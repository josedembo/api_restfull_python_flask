FROM python:3.8-alpine


WORKDIR /ascan-app

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=src
ENV FLASK_ENV=development
ENV SECRET_KEY=dev
ENV FLASK_RUN_PORT=8080
ENV MONGODB_PWD=admin
ENV MONGODB_USER=admin

RUN apk update && apk add --update --no-cache netcat-openbsd && apk add --no-cache make build-base && apk add --no-cache python3-dev && apk add libffi-dev && apk add openssl-dev && apk add curl

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

# RUN curl -sSL https://install.python-poetry.org | python3 - && export PATH="/root/.local/bin:$PATH" && poetry install



EXPOSE  8080

COPY . .

# RUN chmod 755 entrypoint.sh

# ADD ./entrypoint.sh /ascan-app/entrypoint.sh

# ENTRYPOINT ["./entrypoint.sh"]

CMD ["flask", "run"]