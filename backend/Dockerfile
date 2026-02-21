# backend/Dockerfile
FROM python:3.10-slim

# Evita prompts durante instalação de pacotes (Debian)
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Copia o requirements que está dentro de backend/app para a raiz do container
COPY app/requirements.txt .

# Instala dependências de sistema mínimas caso alguma lib precise compilar
# (remova se não precisar)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev build-essential \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Copia todo o conteúdo da pasta backend para /app no container
COPY . .

# Garante que o Python encontre o pacote app/
ENV PYTHONPATH=/app

EXPOSE 8000

# Comando de execução — aponta para app/main.py e a variável 'app'
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
