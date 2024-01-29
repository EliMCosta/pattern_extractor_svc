FROM python:3.11-slim-bullseye

WORKDIR /app

# Copia os arquivos para o diretório atual do contêiner
COPY requirements.txt .
COPY src/ src/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Informa ao Docker que o contêiner irá ouvir na porta 8000
EXPOSE 8000

# Comando para executar a aplicação usando Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
