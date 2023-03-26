from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from tres_D_eehernandezapp.blogApp.models import Pais

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombres, cedula, pais, password=None):
        if not email:
            raise ValueError('el usuario debe tener un email.')

        if not cedula:
            raise ValueError('el usuario debe tener una cedula.')

        user = self.model(
            email=self.normalize_email(email),
            nombres=nombres,
            cedula=cedula,
            pais=pais
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, nombres, cedula, password):
        user = self.create_user(
            email,
            password=password,
            nombres=nombres,
            cedula=cedula,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombres, cedula, password):
        user = self.create_user(
            email,
            password=password,
            nombres=nombres,
            cedula=cedula,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    nombres = models.CharField(max_length=255)
    cedula = models.CharField(max_length=10, unique=True)
    # email = models.CharField(max_length=255, verbose_name='email', unique=True)
    email = models.EmailField(("email address: "), unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['cedula', 'nombres']

    objects = UsuarioManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    class Meta:
        db_table = 'User'
        managed = True