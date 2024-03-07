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
        
        upload_csv = {
            "name": "Upload Mail CSV",
            "object_name": "upload_mail_csv",
            "admin_url": "/mail/upload/csv",
            "view_only": True,
        }
        for app in app_list:
            if app.get("app_label") == "mail":
                app["models"].append(upload_csv)
                break

        app_list += [
            {
                "name": "Classifiers",
                "app_label": "classifiers",
                "models": [
                    {
                        "name": "Logic Classifier",
                        "object_name": "upload_classifier_csv",
                        "admin_url": "/classifiers/logic",
                        "view_only": True,
                    },
                    {
                        "name": "ML Trainer",
                        "object_name": "upload_classifier_csv",
                        "admin_url": "/classifiers/ml/train",
                        "view_only": True,
                    },
                    {
                        "name": "ML Predictor",
                        "object_name": "upload_classifier_csv",
                        "admin_url": "/classifiers/ml/predict",
                        "view_only": True,
                    },
                ],
            }
        ]
        return app_list


minimi_admin_site = MinimiAdminSite(name='minimi_admin')