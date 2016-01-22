"""djcel URL Configuration """
from django.conf.urls import url

from fancy import views

urlpatterns = [
    url(r'^(?P<word>\w+)$', views.expensive_view),
]
