from django.conf.urls import url

from currency_service.currency import views

urlpatterns = [
    url(
        r'^(?P<currency_id>[\w_-]+)/$',
        views.ConverterList.as_view(),
        name='currency_converter_list'
    ),
    url(
        r'^(?P<currency_id>[\w_-]+)/converter'
        r'/(?P<target_currency_id>[\w_-]+)/$',
        views.Converter.as_view(),
        name='currency_converter'
    )
]
