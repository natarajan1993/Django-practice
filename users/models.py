from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) # Every user in the Profile Model is associated with a User from Django so we define that relationship with a OneToOneField
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self): # Overwrite the default save method so we can scale down the image before uploading it
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            img.thumbnail((300,300)) # Use pillow to resize the thumbnail image to 300x300
            img.save(self.image.path)
