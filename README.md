Text Summarizer
==============================

Asynchronous text summarization API using FastAPI.

## API

| Endpoint | HTTP Method | CRUD Method | Description |
| --- | --- | --- | --- |
| /summaries | GET | READ | Get all summaries |
| /summaries/:id | GET | READ | Get a single summary |
| /summaries | POST | CREATE | Add a summary |
| /summaries/:id | PUT | UPDATE | Update a summary |
| /summaries/:id | DELETE | DELETE | Delete a summary |

## Tech
- **Framework** - [FastAPI](https://fastapi.tiangolo.com/)
- **Database** - [PostgreSQL](https://www.postgresql.org/)
- **ORM** - [Tortoise ORM](https://tortoise-orm.readthedocs.io/en/latest/)
- **Testing** - [Pytest](https://docs.pytest.org/en/stable/)
- **Containerization** - [Docker](https://www.docker.com/)
- **CI/CD** - [GitHub Actions](https://github.com/features/actions)
- **Deployment** - [Heroku](https://www.heroku.com/)
