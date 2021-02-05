from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api-auth/', include('rest_framework.urls')),
    url('currency/', include('currency_service.currency.urls')),
    url('product/', include('currency_service.product.urls')),
]
