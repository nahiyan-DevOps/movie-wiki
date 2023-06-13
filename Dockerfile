FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY . /app

RUN pip install -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]