from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from psych import views

app_name = 'psych'

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^new-med/$', views.add_medication, name='new_medication'),
    url(r'^new-medical-diag/$', views.add_medical_diagnosis, name='new_med_diag'),
    url(r'^new-psych-diag/$', views.add_psychological_diagnosis, name='new_psych_diag'),
    url(r'^databoard/', views.databoard, name='databoard'),
    url(r'^testing-center/$', views.testing_center, name='testing_center'),
    url(r'^scales/$', views.scales, name='scales'),
    url(r'^generate-test-code/(?P<subject>\w+)/$', views.generate_test_code, name='generate_test_code'),
    url(r'^nvmt-test-report/(?P<test_code>\w{8})/$', views.nvmt_test_report, name='nvmt_test_report')
]