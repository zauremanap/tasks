FROM python:3.9

WORKDIR /app

COPY . .

CMD ["python", "grad_zaure.py"]
