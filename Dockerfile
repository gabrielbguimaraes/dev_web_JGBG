FROM python:latest

COPY . /app

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ENV FLASK_APP="app.py"

EXPOSE 5000

CMD ["python","-m", "flask", "run", "--host=0.0.0.0"]
