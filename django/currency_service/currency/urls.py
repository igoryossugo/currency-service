from django.conf.urls import url

from currency_service.currency import views

urlpatterns = [
    url(
        r'^(?P<currency_id>[\w_-]+)/converter/$',
        views.Converter.as_view(),
        name='currency_coverter'
    ),
]
