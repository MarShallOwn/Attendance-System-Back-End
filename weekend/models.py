from django.db import models
import uuid
# Create your models here.

class weekend(models.Model):
    id = models.UUIDField(
    primary_key=True,
    unique=True,
    auto_created=True,
    default=uuid.uuid4,
    editable=False,
    null=False,
    blank=False,
    )
    saturday = models.BooleanField(null=False,blank=False)
    sunday = models.BooleanField(null=False,blank=False)
    monday = models.BooleanField(null=False,blank=False)
    tuesday = models.BooleanField(null=False,blank=False)
    wendesday = models.BooleanField(null=False,blank=False)
    thursday = models.BooleanField(null=False,blank=False)
    friday = models.BooleanField(null=False,blank=False)
    def __str__(self):
        return str(self.id)