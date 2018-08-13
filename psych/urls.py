from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'psych'

urlpatterns = [
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^databoard', views.databoard, name='databoard'),
    url(r'^testingcenter', views.testing_center, name='testing_center'),
    url(r'^scales', views.scales, name='scales')
]