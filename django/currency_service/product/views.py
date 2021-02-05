from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from currency_service.backends.pools.catalog import CatalogBackendPool
from currency_service.product.serializers import ProductCurrencySerializer


class ProductCurrencyList(APIView):

    def get(self, request, sku, seller):
        backend = CatalogBackendPool.get_default()
        product = backend.get_product(sku=sku, seller=seller)
        return Response(
            ProductCurrencySerializer(instance=product).data,
            status=status.HTTP_200_OK
        )
