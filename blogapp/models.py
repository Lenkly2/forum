from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now_add=True)

    def published_recently(self):
        today = timezone.now()
        # if today - self.published_date < 7:
        #     return "True"
        a = today - self.published_date
        return a
        
    def __str__(self):
        return self.title
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    author = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name