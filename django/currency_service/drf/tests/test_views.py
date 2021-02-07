import pytest
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

from currency_service.exceptions import APIException


class FakeException(APIException):
    http_status = 500
    error_message = 'Deu ruim'
    error_code = u'fake_error'


class FakeExceptionView(APIView):
    def get(self, request, *args, **kwargs):
        raise FakeException


@pytest.mark.django_db
class TestCustomExceptionHandlerErrorResponse(object):

    def test_should_return_formatted_response_for_P52BaseHttpException(self):
        view = FakeExceptionView.as_view()
        request_factory = APIRequestFactory()

        request = request_factory.get('/')

        response = view(request)

        assert response.status_code == 500
        assert response.data == {
            'error_message': 'Deu ruim',
            'error_code': u'fake_error',
        }
