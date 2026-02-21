FROM node:20-alpine

WORKDIR /app

# Copia os arquivos de dependências
COPY package*.json ./

# Instala as dependências
RUN npm install

# Copia todo o resto dos arquivos da pasta frontend
COPY . .

# Expõe a porta do Vite
EXPOSE 5173

# Comando para rodar o Vite garantindo que ele olhe para a pasta atual
CMD ["npx", "vite", "--host", "0.0.0.0", "--port", "5173"]
