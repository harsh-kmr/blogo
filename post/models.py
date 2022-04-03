from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import datetime
User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
      User,
      on_delete=models.CASCADE, null=True
    )
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='post_like')
    post_time = models.DateTimeField(default=datetime.datetime.now, editable=False)
    def __str__(self):
        return self.title
    
    def preview(self):
      if len(self.body) < 50:
        return self.body
      else:
        return self.body[:50]

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    def total_like(self):
      return self.likes.count()
