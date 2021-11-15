FROM python:3.9.4

RUN pip install pipenv

ENV PROJECT_DIR /intern_V2/intern-api 

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

COPY main.py  main.py ${PROJECT_DIR}/

COPY jokes.json jokes.json ${PROJECT_DIR}/

RUN pipenv install --system --deploy

CMD [ "uvicorn", "/main:app", "--host=0.0.0.0", "--port", "8000", "--reload" ]
