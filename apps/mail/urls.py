from django.urls import path

from . import views

urlspatterns = [
    # upload, with sub paths for csv etc
    # path('upload/', views.upload, name='upload'),
    path('upload/csv/', views.upload_csv, name='upload_csv'),
]
