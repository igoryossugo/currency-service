PORT ?= 8080
TEST_SETTINGS ?= currency_service.settings.test
DEV_SETTINGS ?= currency_service.settings.development
SANDBOX_SETTINGS ?= currency_service.settings.sandbox
PRODUCTION_SETTINGS ?= currency_service.settings.production

MANAGE_PY = django/manage.py

test:
	@pytest django/currency_service

check:
	@flake8 django/
	@isort --check django/

requirements-dev:
	@pip install -r requirements/development.txt

migrate-dev:
	@python $(MANAGE_PY) migrate --settings=$(DEV_SETTINGS)

runserver-dev:
	@python $(MANAGE_PY) runserver --settings=$(DEV_SETTINGS)
