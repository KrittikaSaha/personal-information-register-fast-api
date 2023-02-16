# personal-information-register-fast-api

## 1. Quickstart

### 1.1. Using Docker

To start the API using Docker, follow the following 4 steps:

1. git clone the repo:

```
git clone https://github.com/KrittikaSaha/personal-information-register-fast-api.git

```
2. Run the docker daemon. Depending on the OS, for Windows, one may use Docker Desktop, for LInux and Mac one may use Rancher Desktop. For linux, example step to start running docker daemon manually:
```
sudo systemctl start docker

```
3. Once docker daemon is running, build the image using the dockerfile provided in the repo:

```
docker build -t fastapi_app .

```
4. Now run the Docker image:
```
docker run -p 8000:8000 fastapi_app

```
The API should be running at http://0.0.0.0:8000/docs


### 1.2. Running from local

Pre-requisites: Python3
1. Activate virtualenv

```
virtualenv venv
# For Linux/Mac:
source venv/bin/activate
# For Windows:
. venv/Scripts/activate
```
2. Pip install requirements
```
pip install -r requirements.txt
```
3. cd into /app directory
```
cd app
```
4. Generate data and create database

```
python3 data_generator.py
python3 db.py
```

5. Run the app:
```
uvicorn main:app --reload
```

The API should be running at http://127.0.0.1:8000/docs


## Exploring the functionality of the app

The API has 

### Using curl


### Using Swagger UI



## Explanation of the code 

