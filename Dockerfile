FROM python:3.12.4

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --upgrade --no-cache-dir -r requirements.txt 

COPY . . 

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]    