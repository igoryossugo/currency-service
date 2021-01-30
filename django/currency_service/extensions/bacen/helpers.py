from typing import Dict

from currency_service.backends.cotation.models import Cotation
from currency_service.currency.enums import CurrencyID
from currency_service.extensions.bacen.constants import BACEN_CURRENCY_IDS
from currency_service.extensions.bacen.exceptions import InvalidBacenCurrencyID


def get_bacen_currency_id(currency_id: CurrencyID) -> int:
    try:
        return BACEN_CURRENCY_IDS[currency_id]
    except KeyError:
        raise InvalidBacenCurrencyID(currency_id)


def build_cotation_by_bacen_response(
    target_currency: CurrencyID,
    source_currency: CurrencyID,
    response_target_cotation: Dict,
    response_source_cotation: Dict = None,
) -> Cotation:
    target_cotation = (
        response_target_cotation['ultimoValor']['valor']['_value_1']
    )

    if not response_source_cotation:
        return Cotation(
            value=target_cotation,
            source_currency=source_currency,
            target_currency=target_currency
        )

    source_cotation = (
        response_source_cotation['ultimoValor']['valor']['_value_1']
    )
    value = target_cotation / source_cotation

    return Cotation(
        value=value,
        source_currency=source_currency,
        target_currency=target_currency
    )
