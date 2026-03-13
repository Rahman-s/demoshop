from django.db import models

class Shoe(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, default="General")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Main product image
    image = models.ImageField(upload_to='shoes/')
    
    # Banner ke liye - Isme aap Video ya Photo dono upload kar sakte hain
    # Cloudinary isse FileField ke through handle kar lega
    banner_video = models.FileField(
        upload_to='banners/', 
        null=True, 
        blank=True, 
        help_text="Upload a Video (.mp4) or a High-Res Image for the hero banner."
    )
    
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] # Naye shoes hamesha pehle dikhenge

    def __str__(self):
        return f"{self.brand} - {self.name}"
