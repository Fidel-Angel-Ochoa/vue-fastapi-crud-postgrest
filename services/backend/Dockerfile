FROM python:3.11-buster

RUN mkdir app
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=/app
ENV PORT=8000

# this lines must be delete if you gonna use the dockerfile to build the container and deploy it in a server and/or push to github
# to use localy you can use like this:
ENV DATABASE_URL=postgres://hello_fastapi:2UbGuBJjOBp4e8oZPC3UzLyggKjaDDh3@dpg-cj9i5uivvtos73ei5ng0-a.oregon-postgres.render.com/hello_fastapi
ENV SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7



ENV PYTHONUNBUFFERED True


EXPOSE 8000

COPY migrations .
COPY pyproject.toml .

# in this line was an error, was copying to /. and the structure of the project need that the docker container has 'src' too.
COPY ./src/ ./src 

# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 src.main:app
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
# CMD uvicorn src.main:app --reload --port=80 --host=0.0.0.0 