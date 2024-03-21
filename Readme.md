# Statistics module

This microservice contains API's to put, get, create, update, delete information about the shoots on the module. 

## Before running the server

Steps to run the repo: 
1. Install the requirements 
```bash 
pip install -r requirements.txt
```
2. Run the docker compose file to build the mongoDB image
```bash
cd ./docker/
docker-compose up -d   # Or sudo docker-compose up -d
```
## Run the server
3. Run the uvicorn server
```bash
cd ./src
uvicorn main:app
```
4. On your browser open `localhost:8000/docs`

## Run the tests
5. Use pytest to run tests
```bash
pytest
```
