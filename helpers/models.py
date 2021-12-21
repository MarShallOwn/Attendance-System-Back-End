from django.db import models
class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        #enable us to order the object with create_at
        abstract=True
        ordering=('-created_at',)
