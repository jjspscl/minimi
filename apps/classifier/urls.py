from django.urls import path, include

from . import views

ml_patterns = [
    path('train/', views.ml_train, name='ml_train'),
    path('predict/', views.ml_predict, name='ml_predict'),
]

urlspatterns = [
    path('logic/', views.logic_classifier, name='logic_classifier'),
    path('ml/', include(ml_patterns)),
]
