FROM python:3.10-slim

# Define o diretório de trabalho como /app
WORKDIR /app

# Copia o requirements da raiz do backend para o container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo da pasta backend para /app no container
COPY . .

# Define a variável de ambiente para o Python encontrar o módulo 'app'
ENV PYTHONPATH=/app

EXPOSE 8000

# Comando explícito apontando para a pasta app e o arquivo main
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
