from django.db import models

# Create your models here.
class Email(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()

    def __str__(self):
        preview = self.content[:15]
        return f"{self.id}-{preview}..."