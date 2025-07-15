from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class CustomUserManager(UserManager):
    @staticmethod
    def _resolve_role(value):
        if isinstance(value, Role):
            return value
        try:
            return Role.objects.get(id=value)
        except (ValueError, ObjectDoesNotExist):
            return Role.objects.get(name=value)

    def create_user(self, username, password, **extra_fields):
        extra_fields['role'] = self._resolve_role(extra_fields.get('role'))
        return super().create_user(username=username, password=password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields['role'] = Role.objects.get(name='Owner')
        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True
        return super().create_superuser(username=username, password=password, **extra_fields)


class User(AbstractUser):
    role = models.ForeignKey(Role, null=False, blank=False, on_delete=models.PROTECT)

    REQUIRED_FIELDS = ['role', 'email']

    objects = CustomUserManager()

    def is_seeker(self):
        print(self.role.name)
        return self.role.name == 'Seeker'

    def is_owner(self):
        print(self.role.name)
        return self.role.name == 'Owner'