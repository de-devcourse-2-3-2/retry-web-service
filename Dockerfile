FROM python:3.11
WORKDIR /retry-web-service
COPY ./crawling /retry-web-service/crawling
COPY ./musinsa_trend /retry-web-service/musinsa_trend
COPY ./requirements.txt /retry-web-service
COPY ./logger.py /retry-web-service
RUN apt-get update
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /retry-web-service/musinsa_trend
#CMD ["python3", "manage.py", "runserver", "localhost:8000"]
CMD ["python3", "manage.py", "migrate"]
#EXPOSE 8000