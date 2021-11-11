# Dockerfile, Image, Container
FROM python:3.9.4

ADD main.py .

CMD ["python", "./main.py"]