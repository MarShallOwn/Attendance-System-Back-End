from django.db import models
import uuid
class Control(models.Model):
    id = models.UUIDField(
    primary_key=True,
    unique=True,
    auto_created=True,
    default=uuid.uuid4,
    editable=False,
    null=False,
    blank=False,
    )
    checkinMinTime = models.TimeField(blank=False,null=False)
    checkinMaxTime = models.TimeField(blank=False,null=False)
    checkoutMinTime = models.TimeField(blank=False,null=False)
    checkoutMaxTime = models.TimeField(blank=False,null=False)
    numOfLeaveRequest = models.IntegerField(blank=False,null=False)
    def __str__(self):
        return str(self.id)