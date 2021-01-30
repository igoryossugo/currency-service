PORT ?= 8080
TEST_SETTINGS ?= currency.settings.test
DEV_SETTINGS ?= currency.settings.development
SANDBOX_SETTINGS ?= currency.settings.sandbox
PRODUCTION_SETTINGS ?= currency.settings.production

MANAGE_PY = django/manage.py

test:
	@pytest django/currency

migrate-dev:
	@python $(MANAGE_PY) migrate --settings=$(DEV_SETTINGS)

runserver-dev:
	@python $(MANAGE_PY) runserver --settings=$(DEV_SETTINGS)
