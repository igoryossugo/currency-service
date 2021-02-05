from rest_framework.response import Response
from rest_framework.views import exception_handler

from currency_service.exceptions import APIException


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if _is_custom_exception(response, exc):
        response = _create_payload_for_custom_exceptions(exc)

    return response


def _is_custom_exception(response, exception):
    return response is None and isinstance(exception, APIException)


def _create_payload_for_custom_exceptions(exception):
    payload = {
        'error_message': exception.error_message,
        'error_code': exception.error_code
    }

    return Response(payload, status=exception.http_status)
