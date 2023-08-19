FROM python:3.11-buster

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.
ENV PORT=80


ENV PYTHONUNBUFFERED True

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

COPY migrations .
COPY pyproject.toml .

COPY src/ .

# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 src.main:app
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
# CMD uvicorn src.main:app --reload --port=80 --host=0.0.0.0 