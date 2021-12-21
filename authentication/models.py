
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
#import Tracking model from helper that track(created,updated) date
from helpers.models import TrackingModel
#this imports allow us to inherit the django User model and modify it.
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, UserManager
#used to restrict us from creating wrong username that contains "@,%m..etc"
from django.contrib.auth.validators import UnicodeUsernameValidator
# A registry that stores the configuration of installed applications.
# It also keeps track of models, e.g. to provide reverse relations.
from django.apps import apps
#to has the user password
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
#to work with date
from django.utils import timezone
#allow me to change defualt id with uuid with unsequintial number
import uuid as uuid_lib
#Used to generate the access and the refresh token
from rest_framework_simplejwt.tokens import RefreshToken
#models the user has relation with 
from role.models import role

class MyUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin,TrackingModel):
    username_validator = UnicodeUsernameValidator()
    id=models.UUIDField(
        default=uuid_lib.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
        auto_created=True,
        null=False,
        blank=False,
    )
    nationalID = models.CharField(
        _('National ID'),
        max_length=14,
        unique=True,
        help_text=_('National Id must be 14 char'),
        validators=[MinLengthValidator(limit_value=14,message='National ID must be 14 char')],
        error_messages={'unique':'user with this national id already exists'},blank=False,null=False,
        )
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },blank=False,null=False,
    )
    firstname = models.CharField(_('first name'), max_length=150,blank=False,null=False,)
    lastname = models.CharField(_('last name'), max_length=150,blank=False,null=False,)
    email = models.EmailField(_('email address'),unique=True,blank=False,null=False,)
    phoneNumber = models.CharField(
        _('phone number'),
        max_length=11,
        validators=[MinLengthValidator(limit_value=11,message='Phone Number must be 11 number'),RegexValidator(regex=r'01[1,2,5,0]{1}[0-9]{8}',message="must be valid Egyption Number")],
        unique=True,
    error_messages={
            'unique': _("A user with that phone number already exists."),
        },
    blank=False,
    null=True,
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    role = models.ForeignKey(role,related_name='user',on_delete=models.SET_NULL,blank=False,null=True)
    department = models.ForeignKey('department.department',on_delete=models.SET_NULL,blank=False,null=True)
    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    #used to generate token when call it
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access':str(refresh.access_token),
        }
    def __str__(self):
        return str(self.id)