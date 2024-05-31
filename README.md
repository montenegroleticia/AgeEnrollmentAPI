## Age groups enrollment API

This project implements an API for managing age groups and processing enrollments.

### Tools
<img align = "center" alt = "Node.js" src = "https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/> <img align = "center" alt = "Node.js" src = "https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/> <img align = "center" alt = "Node.js" src = "https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/>

### API Documentation

### Age Groups

- **Register a new age group**
  - **POST** `/age-groups/`
  - Request Body:
    ```json
    {
      "min_age": 10,
      "max_age": 15
    }
    ```

- **Delete an age group**
  - **DELETE** `/age-groups/{age_group_id}`

- **View existing age groups**
  - **GET** `/age-groups/`

### Enrollments

- **Request enrollment**
  - **POST** `/enrollments/`
  - Request Body:
    ```json
    {
      "name": "Maria",
      "age": 21,
      "cpf": "12345678900"
    }
    ```

- **Check enrollment status**
  - **GET** `/enrollments/{enrollment_id}/status`

- **View existing enrollment**
  - **GET** `/enrollments/`

### How to run

1. Clone this repository:

```bash
git clone https://github.com/montenegroleticia/AgeEnrollmentAPI.git
```

2. Copy the example environment file and configure the environment variables:

```bash
cp .env.example .env
```

3. Build:

```bash
docker compose build
```

4. Run API and DB:

```bash
docker compose up
```

5. Access aplication:
```bash
localhost:8000
```

6. Run tests with pytest:

```bash
docker compose run api pytest
```

7. Run lint with flake8:

```bash
docker compose run api flake8
```
