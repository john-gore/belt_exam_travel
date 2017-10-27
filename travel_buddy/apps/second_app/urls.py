from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url (r'^$', views.index, name="index"),
    url (r'^destination$', views.destination, name="destination"),
]