FROM python:3.13.2

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . .

# Instale as dependências
RUN pip install --no-cache-dir requests beautifulsoup4

# Execute o script
ENTRYPOINT ["python", "lista_parceiros.py"]


