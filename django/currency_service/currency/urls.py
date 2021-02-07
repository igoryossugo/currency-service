from django.conf.urls import url

from currency_service.currency import views

urlpatterns = [
    url(
        r'^(?P<currency_id>[\w_-]+)/$',
        views.ConvertList.as_view(),
        name='currency_convert_list'
    ),
    url(
        r'^(?P<currency_id>[\w_-]+)/convert'
        r'/(?P<target_currency_id>[\w_-]+)/$',
        views.Convert.as_view(),
        name='currency_convert'
    )
]
