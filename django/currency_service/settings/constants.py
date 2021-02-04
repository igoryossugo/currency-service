
########
# TIME #
########
SECONDS = 1
MINUTES = 60 * SECONDS
HOURS = 60 * MINUTES
DAYS = 24 * HOURS

############
# BACKENDS #
############

FAKE_CATALOG_BACKEND = 'currency_service.extensions.fake.backends.catalog.FakeCatalogBackend'  # noqa

FAKE_COTATION_BACKEND = 'currency_service.extensions.fake.backends.cotation.FakeCotationBackend'  # noqa
BACEN_COTATION_BACKEND = 'currency_service.extensions.bacen.backend.BacenCotationBackend'  # noqa
