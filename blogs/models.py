from django.db import models
from django.contrib.auth import get_user_model
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
    
class Blog(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.TextField()
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'blogs'

    def __str__(self):
        if len(self.text) > 50:
            return self.text[:10] + '...'
        else:
            return self.text