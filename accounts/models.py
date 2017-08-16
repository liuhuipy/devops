from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.


class PermissionList(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)

    class Meta:
        verbose_name = u'权限'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}({})'.format(self.name, self.url)

    def get_permission(self):
        return self.name


class RoleList(models.Model):
    name = models.CharField(max_length=64)
    permission = models.ManyToManyField(PermissionList, blank=True)

    class Meta:
        verbose_name = u'角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractUser):
    email = models.EmailField(max_length=255,unique=True,verbose_name=u'邮箱')
    username = models.CharField(max_length=32,unique=True,verbose_name=u'用户名')
    password = models.CharField(max_length=128,verbose_name=u'密码')
    role = models.ForeignKey(RoleList, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    object = MyUserManager()
    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):  # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


