from django.urls import path, include
from . import views

app_name = 'project_api'

urlpatterns = [
    path('', views.project_api, name='project_api'),
]