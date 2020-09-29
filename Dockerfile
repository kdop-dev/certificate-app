FROM python:3-alpine

WORKDIR /app

COPY ./app /app

RUN pip install -r /app/requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]
