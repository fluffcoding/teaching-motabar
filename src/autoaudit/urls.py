from django.contrib import admin
from django.urls import path

from reports.views import index, create_report, single_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('report/<id>', single_report, name='single-report'),
    path('', index, name='index'),
    path('create-report', create_report, name='create-report')

]
