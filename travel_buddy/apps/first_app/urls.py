from django.conf.urls import url
from .models import User, Trip
from . import views           
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'register$', views.register, name='register'),
    url(r'login$',views.login, name='login'),
    url(r'success$', views.success, name='success'),
    url (r'^add_trip$', views.add_trip, name="add_trip"),
    url(r'^dash$', views.dash, name='dash'),
    url(r'^first_app/(?P<id>\d+)adddestination$', views.adddestination, name='adddestination'),  
]