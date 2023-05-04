from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.title + " created on " + str(self.created_at)
