# FastAPI App

API simple hecha con FastAPI y Docker.

## Ejecutar

1. Construir la imagen:

docker build -t fastapi-app .

2. Ejecutar el contenedor 
docker run -d -p 8000:8000 fastapi-app

3. Abrir en el navegador
http://localhost:8000/docs