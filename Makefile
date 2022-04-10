init:
	pip install pipenv
	pipenv install --dev

run:
	pipenv run NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn app.main:app --workers=4 --bind 0.0.0.0:5000 --reload

test:
	pipenv run pytest tests/unit

integration-test:
	pipenv run pytest tests/integration

# TODO: Implement tests
# coverage:
# 	pipenv run pytest tests/unit --doctest-modules --junitxml=junit/test-results.xml --cov=app --cov-report=xml --cov-report=html

lint:
	pipenv run pylint app

backup-db:
	docker compose exec -T db pg_dumpall -c -U todolist_app > dump.sql

restore-db:
	cat dump.sql | docker compose exec -i db psql -U todolist_app

requirements:
	pipenv lock -r > requirements.txt
