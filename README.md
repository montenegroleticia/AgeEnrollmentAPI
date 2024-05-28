### Age groups enrollment API

This project implements an API for managing age groups and processing enrollments.

#### Tools
<img align = "center" alt = "Node.js" src = "https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/> <img align = "center" alt = "Node.js" src = "https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/> <img align = "center" alt = "Node.js" src = "https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/>

#### API Documentation

#### How to run

1. Copy the example environment file and configure the environment variables:

```sh
cp .env.example .env
```

2. Build:

```bash
docker compose build
```

3. Run API:

```bash
docker compose up
```

4. Access aplication:
```bash
localhost:8000
```

3. Run tests with pytest:

```bash
docker compose run api pytest
```

4. Run lint with flake8

```bash
docker compose run api flake8
```
