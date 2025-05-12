# Student Course Management API

## Features
- Create and retrieve students and courses
- Enroll students in courses
- Email validation
- Pagination
- SQLite/PostgreSQL support
- Unit tests

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Testing API

```bash
bash test_api.sh
```

## Run Unit Tests

```bash
pytest
```
