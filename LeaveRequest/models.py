from decimal import MAX_PREC
import uuid
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.fields import TextField
from dateutil.relativedelta import relativedelta
from datetime import datetime

# Create your models here.
class LeaveRequest(models.Model):
    id = models.UUIDField(
    primary_key=True,
    unique=True,
    auto_created=True,
    default=uuid.uuid4,
    editable=False,
    null=False,
    blank=False,
    )
    typeOfLeave = models.CharField(max_length=100,validators=[MinLengthValidator(limit_value=2,message='Leave Request Type greater than 2 char')],blank=False,null=False)
    description = TextField(blank=False,null=False)
    startDate = models.DateField(blank=False,null=False,)
    endDate = models.DateField(blank=False,null=False)
    status = models.CharField(max_length=100,validators=[MinLengthValidator(limit_value=2,message='status greater than 2 char')],blank=False,null=False)
    user = models.ForeignKey('authentication.User',related_name='leaevRequest',on_delete=models.CASCADE,blank=False,null=False)
    @property
    def numOfDay(self):
        return relativedelta(self.startDate.days, self.endDate.days)
    def __str__(self):
        return str(self.id)