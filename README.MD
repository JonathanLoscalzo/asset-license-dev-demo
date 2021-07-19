

# ACME

## Backend

It is developed with _FastAPI_ and MongoDB.
Python version: 3.9.2

### Development

Install on your venv, poetry:
```
pip install poetry
```

Then, just run it: 

```
poetry install --no-dev
poetry run start
```

or

```
python src/asset_manager/main.py
```


### Docker

```
docker-compose -f docker-compose.yml up -d backend db
# navigate to localhost:8000/docs and localhost:8000/redocs
```

## Frontend

NodeJS version: v14 (using NVM)

```
npm run start
```

### Docker
```
docker-compose -f docker-compose.yml up -d frontend
# navigate to localhost:3000
```


