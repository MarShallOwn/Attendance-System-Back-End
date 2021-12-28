from django.db import models
from authentication.models import User
import uuid
from helpers.models import TrackingModel

# Create your models here.

class department(TrackingModel):
    id = models.UUIDField(
    primary_key=True,
    unique=True,
    auto_created=True,
    default=uuid.uuid4,
    editable=False,
    null=False,
    blank=False,
    ) 
    departmentName = models.CharField(max_length=20,blank=False,null=False)
    departmentDesc = models.TextField(blank=False,null=False)
    departmentHeadID = models.OneToOneField(User,related_name='headOnDepartment',on_delete=models.SET_NULL,null=True,blank=False)
    def __str__(self):
        return str(self.id)