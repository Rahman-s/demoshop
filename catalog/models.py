from django.db import models

class Shoe(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, default="General") # Brand field missing thi
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # Price field check karein
    image = models.ImageField(upload_to='shoes/')
    banner_video = models.FileField(upload_to='videos/', null=True, blank=True)
    is_available = models.BooleanField(default=True) # Yeh field missing thi
    created_at = models.DateTimeField(auto_now_add=True) # Yeh field missing thi

    def __str__(self):
        return self.name
