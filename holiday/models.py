from django.db import models
from django.db import models
import uuid
from django.core.validators import MinLengthValidator
# Create your models here.

class holiday(models.Model):
    id = models.UUIDField(
    primary_key=True,
    unique=True,
    auto_created=True,
    default=uuid.uuid4,
    editable=False,
    null=False,
    blank=False,
    )
    name = models.CharField(max_length=100,validators=[MinLengthValidator(limit_value=2,message='name cannot be less than 2 char')],null=False,blank=False)
    type = models.CharField(max_length=100,validators=[MinLengthValidator(limit_value=2,message='type cannot be less than 2 char')],null=False,blank=False)
    startDate = models.DateField(blank=False,null=False)
    noOfDays = models.PositiveIntegerField(blank=False,null=False)
    endDate = models.DateField(blank=False,null=False)
    def __str__(self):
        return str(self.id)