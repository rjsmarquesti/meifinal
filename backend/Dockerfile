FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

# CORREÇÃO: Busca o arquivo na raiz da pasta backend
COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev build-essential \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY . .

ENV PYTHONPATH=/app
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
