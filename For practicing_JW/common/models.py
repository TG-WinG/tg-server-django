from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not username:
            raise ValueError('반드시 아이디를 포함해야 합니다.')
        if not email:
            raise ValueError('반드시 이메일을 포함해야 합니다.')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_doctor(self,username,email,password):
        if not username:
            raise ValueError('반드시 아이디를 포함해야 합니다.')
        if not email:
            raise ValueError('반드시 이메일을 포함해야 합니다.')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        user.is_doctor=True
        return user
    
    def create_superuser(self,username,email,password):
        user = self.create_user(
            username,email,
            password=password,
        )
        user.is_admin=True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    username=models.CharField(
        verbose_name='아이디',
        max_length=10,
        unique=True,
    )
    email=models.EmailField(
        verbose_name='이메일',
        max_length=255,
        unique=True,
    )
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects=UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    def is_doc(self):
        return self.is_doctor

# Create your models here.
