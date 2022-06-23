from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_('date of birthday'))
    city = models.CharField(max_length=30, default=None, null=True, verbose_name=_('city'))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = _('users')
        verbose_name = _('user')
