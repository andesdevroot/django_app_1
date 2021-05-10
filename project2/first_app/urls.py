from django.conf.urls import url
from first_app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url('', views.index, name='index')
]

