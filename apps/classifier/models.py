from django.db import models

class MLModel(models.Model):
    name = models.CharField(max_length=255)
    model_file = models.FileField(upload_to='models/')

    def __str__(self):
        return self.name
