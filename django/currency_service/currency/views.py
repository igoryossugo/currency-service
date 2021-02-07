from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from currency_service.currency.models import Currency
from currency_service.currency.serializers import (
    CurrencySerializer,
    CurrencyValueSerializer
)


class Convert(APIView):

    def post(self, request, currency_id, target_currency_id):
        serializer = CurrencyValueSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        currency = Currency(
            id=currency_id.upper(),
            value=serializer.validated_data['value']
        )
        currency.convert(id=target_currency_id.upper())

        return Response(
            CurrencySerializer(instance=currency).data,
            status=status.HTTP_200_OK
        )


class ConvertList(APIView):

    def post(self, request, currency_id):
        serializer = CurrencyValueSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        currencies = Currency.convert_list(
            id=currency_id.upper(),
            value=serializer.validated_data['value']
        )
        return Response(
            CurrencySerializer(instance=currencies, many=True).data,
            status=status.HTTP_200_OK
        )
