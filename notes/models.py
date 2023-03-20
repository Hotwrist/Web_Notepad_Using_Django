from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    memory = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    #uncomment when using function based view
    #class Meta:
    #    ordering = ['-date_posted']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("note-detail", kwargs={"pk": self.pk})
    