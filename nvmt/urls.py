from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path

from . import views

app_name = 'nvmt'

urlpatterns = [
    url(r'^', views.home, name='home'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^register-subject/', views.register_subject, name='register_subject'),
    url(r'^test-completed/', views.test_finished, name='test_finished'),
]