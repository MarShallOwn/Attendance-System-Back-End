from django.db import models
from authentication.models import User
import uuid

# Create your models here.
class attendence(models.Model):
    id = models.UUIDField(
    primary_key=True,
    unique=True,
    auto_created=True,
    default=uuid.uuid4,
    editable=False,
    null=False,
    blank=False,
    )
    didAttended = models.BooleanField(default=True,blank=False,null=False)
    checkIn = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    checkOut = models.TimeField()
    Date = models.DateField(auto_now_add=True,blank=False,null=False)
    userId = models.ForeignKey(User,related_name='attendence',on_delete=models.CASCADE,null=False,blank=False)
def __str__(self):
        return str(self.id)