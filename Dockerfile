# Utilizamos una imagen base de Debian para aprovechar las bibliotecas de Intel incluidas
FROM python:3.8-slim-buster

# Seteamos el directorio de trabajo
WORKDIR /app

# Copiamos el código fuente al contenedor
COPY . .

# Comando para ejecutar la aplicación o script
CMD ["python", "main.py"]
