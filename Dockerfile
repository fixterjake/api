FROM python:3.10-slim

EXPOSE 8000
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

CMD python -m uvicorn --host=0.0.0.0 app.main:app
