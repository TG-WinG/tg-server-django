from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self,student_id,email,phone_number,name,semester,password=None):
        if not student_id:
            raise ValueError('반드시 학번을 포함해야 합니다.')
        if not email:
            raise ValueError('반드시 이메일을 포함해야 합니다.')
        if not password:
            raise ValueError('반드시 패스워드를 포함해야 합니다.')
        user = self.model(
            student_id=student_id,
            phone_number=phone_number,
            name=name,
            semester=semester,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self,student_id,email,phone_number,name,semester,password):
        user = self.create_user(
            student_id,email,phone_number,name,semester,password
        )
        user.is_admin=True
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractBaseUser):
    student_id=models.CharField(
        verbose_name='학번',
        max_length=10,
        unique=True,
    )
    email=models.EmailField(
        verbose_name='이메일',
        max_length=255,
        unique=True,
    )
    name=models.CharField(
        verbose_name='이름',
        max_length=10,
    )
    is_active=models.BooleanField(default=True) # 계정 활성화 권한 변경하지 말것!
    status=models.BooleanField(default=True) # 재학 상태 여부
    is_admin=models.BooleanField(default=False)
    is_email_activated=models.BooleanField(default=False) # 이메일 인증 여부
    semester=models.CharField(
        verbose_name='학기',
        max_length=3,
        default='1-1',
    )
    phone_number=models.CharField(
        verbose_name='전화번호',
        max_length=11,
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['student_id','name','semester','phone_number']
    objects=UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def return_email(self):
        return self.email
    
    @property
    def is_staff(self):
        return self.is_admin
    

# Create your models here.
