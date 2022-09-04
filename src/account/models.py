from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


class AccountManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        user = self.create_user(email, password, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class AccountCustom(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email"), max_length=254, unique=True)
    username = models.CharField(_("username"), max_length=50)
    is_staff = models.BooleanField(_("is_staff"), default=False)
    is_superuser = models.BooleanField(_("is_superuser"), default=False)
    is_active = models.BooleanField(_("is_active"), default=False)
    objects = AccountManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(AccountCustom, on_delete=models.CASCADE)
    phone = models.CharField(_("phone"), max_length=50,null=True,blank=True)
    city = models.CharField(_("city"), max_length=50,null=True,blank=True)
    zipcode = models.CharField(_("zipcode"), max_length=50,null=True,blank=True)
    addr1 = models.TextField(_("address1 "),null=True,blank=True)
    addr2 = models.TextField(_("address2 "),null=True,blank=True)
    
    def __str__(self):
        return self.user.email
    


@receiver(post_save, sender=AccountCustom)
def profile_post_save(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
