from django.urls import path

from . import views

urlspatterns = [
    path('table/', views.email_table, name='email_table'),
    path('upload/csv/', views.upload_csv, name='upload_csv'),
]
