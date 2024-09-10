from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title