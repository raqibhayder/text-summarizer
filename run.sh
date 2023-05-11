docker-compose down -v
docker-compose up -d --build
docker-compose exec web aerich upgrade
docker-compose exec web python -m pytest
docker-compose exec web python -m pytest --cov="."
docker-compose exec web flake8 .
docker-compose exec web black . --check
docker-compose exec web black .
docker-compose exec web isort . --check-only
docker-compose exec web isort .