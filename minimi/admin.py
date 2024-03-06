from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _

class MinimiAdminSite(admin.AdminSite):
    site_title = _('jjspscl')
    index_title = _('Minimi - Django Email Classifier Application')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = []
        return urls + custom_urls

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        app_list += [
            {
                "name": "Mail",
                "app_label": "mail",
                # "app_url": "/admin/mail",
                "models": [
                    {
                        "name": "Upload Mail CSV",
                        "object_name": "upload_mail_csv",
                        "admin_url": "/mail/upload/csv",
                        "view_only": True,
                    }
                ],
            }
        ]
        return app_list


minimi_admin_site = MinimiAdminSite(name='minimi_admin')
