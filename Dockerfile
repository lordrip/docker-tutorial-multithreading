FROM python:3

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypy.python.org -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "app.py"]
