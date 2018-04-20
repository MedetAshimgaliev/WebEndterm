from django.db import models
from django.utils import timezone

class postapi(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    post_id = models.IntegerField()
    created_at = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
