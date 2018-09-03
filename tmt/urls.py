from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'tmt'

urlpatterns = [
    url(r'^$', views.test_home, name='test_home'),
    url(r'^test-start/(?P<test_code>\w{8})/$', views.test_start, name='test_start'),
    url(r'^test-data/(?P<test_code>\w{8})/$', views.send_test_data, name='test_data'),
]