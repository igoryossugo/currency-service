from currency_service.product import views
from django.conf.urls import url

urlpatterns = [
    url(
        r'currency/(?P<sku>[\w_-]+)/seller/(?P<seller>[\w_-]+)/$',
        views.ProductCurrencyList.as_view(),
        name='product_currency_list'
    )
]
