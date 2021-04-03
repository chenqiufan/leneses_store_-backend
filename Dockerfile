FROM python:3.8.2
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 59003
CMD ["python","run.py"]