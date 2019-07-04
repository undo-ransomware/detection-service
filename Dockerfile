FROM python:3.6

WORKDIR /detection-service
COPY . .

RUN pip install -r requirements.txt
CMD ["python", "wsgi.py"]