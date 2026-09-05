sources: https://ajeetraina.medium.com/getting-started-with-fastapi-and-docker-ec6dd498d669

create python virtual environment: python -m venv venv

activate virtual environment in backend folder(Powershell): venv\Scripts\activate

install dependencies: pip install -r requirements.txt

build docker image from dockerfile: docker build -t recipe-backend

run docker container: docker run -p 8000:80 recipe-backend

connection url for postgres: "postgresql://USERNAME:PASSWORD@localhost:PORT/DBNAME"