# Matching-Service

Create python virtual environment
```python3 -m venv pj1```

Activate the virtual environment, install all the packages and launch the backend service
```
source pj1/bin/activate
pip3 install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

Or use docker

```
docker build -t matching-service .

docker run -d -p 8001:8001 matching-service
```