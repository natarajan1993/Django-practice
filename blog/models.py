from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE) # Define a relationship between the author of the post and Django's pre-built User model. So the author is a foreign key inherited from the User model. If the user is deleted, then delete the post as well
    
    def __str__(self):
        return self.title

    def get_absolute_url(self): # Re-route the user to the post that was just created after they create the post
    	return reverse('post-detail', kwargs = {'pk':self.pk})