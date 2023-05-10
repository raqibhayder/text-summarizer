Text Summarizer
==============================

![Continuous Integration and Delivery](https://github.com/raqibhayder/text-summarizer/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=main)


Asynchronous text summarization API using FastAPI.

## API

| Endpoint | HTTP Method | CRUD Method | Description |
| --- | --- | --- | --- |
| /summaries | GET | READ | Get all summaries |
| /summaries/:id | GET | READ | Get a single summary |
| /summaries | POST | CREATE | Add a summary |
| /summaries/:id | PUT | UPDATE | Update a summary |
| /summaries/:id | DELETE | DELETE | Delete a summary |

## Stack
- **Framework** - [FastAPI](https://fastapi.tiangolo.com/)
- **Database** - [PostgreSQL](https://www.postgresql.org/)
- **ORM** - [Tortoise ORM](https://tortoise-orm.readthedocs.io/en/latest/)
- **Testing** - [Pytest](https://docs.pytest.org/en/stable/)
- **Containerization** - [Docker](https://www.docker.com/)
- **CI/CD** - [GitHub Actions](https://github.com/features/actions)
- **Deployment** - [Heroku](https://www.heroku.com/)
- **Code Coverage** - [Coverage.py](https://coverage.readthedocs.io/en/7.2.5/)
  - **pytest-cov** - [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
- **Code Quality** - [flake8](https://flake8.pycqa.org/en/latest/)
- **Code Formatting** - [black](https://black.readthedocs.io/en/stable/)
