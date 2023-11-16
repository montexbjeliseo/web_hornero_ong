from django.db import models

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images')
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption