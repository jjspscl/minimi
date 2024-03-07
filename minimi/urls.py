from django.contrib import admin
from django.urls import path, include
from .admin import minimi_admin_site
from apps.mail import urls as mail_urls
from apps.classifier import urls as classifier_urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', minimi_admin_site.urls),
    path('mail/', include(mail_urls.urlspatterns)),
    path('classifiers/', include(classifier_urls.urlspatterns)),
]
