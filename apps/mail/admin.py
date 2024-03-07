from django.contrib import admin
from minimi.admin import minimi_admin_site
from .models import Email

minimi_admin_site.register(Email)
# Register your models here.
