FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de dependências
COPY backend/requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo da pasta backend para dentro do container
COPY backend/ .

# Expõe a porta que o seu app usa (geralmente 8000 ou 80)
EXPOSE 8000

# Comando para rodar o servidor (ajuste 'app.main:app' se o seu arquivo principal for outro)
# Se o seu arquivo principal for main.py e a variável do app for 'app':
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
