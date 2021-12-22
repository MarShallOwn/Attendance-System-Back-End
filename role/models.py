from django.db import models
import uuid

# Create your models here.
class role(models.Model):
    id = models.UUIDField(
    primary_key=True,
    unique=True,
    auto_created=True,
    default=uuid.uuid4,
    editable=False,
    null=False,
    blank=False,
    )
    roleName = models.CharField(max_length=30,unique=True,blank=False,null=False)
    roleDesc = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.id)

