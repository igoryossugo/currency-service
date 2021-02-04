from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from currency_service.currency.models import Currency
from currency_service.currency.serializers import CurrencySerializer


class Converter(APIView):

    def post(self, request, currency_id):
        serializer = CurrencySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        currency = Currency(
            id=currency_id.upper(),
            value=serializer.validated_data['value']
        )
        currency.converter(id=serializer.validated_data['id'])

        return Response(
            CurrencySerializer(instance=currency).data,
            status=status.HTTP_200_OK
        )
