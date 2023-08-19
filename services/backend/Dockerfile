FROM python:3.11-buster

RUN mkdir app
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=/app
ENV PORT=8000



ENV PYTHONUNBUFFERED True


EXPOSE 8000

COPY migrations .
COPY pyproject.toml .

# in this line was an error, was copying to /. and the structure of the project need that the docker container has 'src' too.
COPY ./src/ ./src 

# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 src.main:app
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
# CMD uvicorn src.main:app --reload --port=80 --host=0.0.0.0 