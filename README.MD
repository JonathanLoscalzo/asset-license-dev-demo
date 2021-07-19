

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


## Built Status:

Backend:
- [x] CRUD Developers
- [x] add/remove assets from a developer
- [x] add/remove licenses from a developer
- [x] active/deactive developer
- [x] auth with credentials -> admin:secure


Frontend:
- [x] modules architecture
- [x] auth form
- [x] logout
- [x] create dev
- [x] list devs
- [x] list assets
- [x] list licenses
- [ ] add/remove assets/licenses from a developer
- [ ] remove a developer
- [ ] active/deactive a developer

General:
- backend: fastapi, poetry, pymongo, layered architecture
    - Navigate to swagger: localhost:8000/docs and localhost:8000/redocs
- frontend: react, reactstrap, formik, router, module architecture
    - Navigate to frontend: localhost:3000
- DB: mongodb
    - Exposed in 27017
- Docker integration: ```docker-compose -f docker-compose.yml up -d```

