FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./ ./

RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8000

CMD [ "python", "intelligent_systems/manage.py", "runserver", "0.0.0.0:8000" ]
