from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ERISA_User(AbstractUser):
    id = models.PositiveBigIntegerField(primary_key=True, validators=[MaxValueValidator(999999)])

    groups = models.ManyToManyField(
        Group,
        related_name="erisa_user_set",  # avoid clash
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="erisa_user_permissions_set",  # avoid clash
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    class Meta:
        db_table = "users"