import datetime

from rest_framework_sudo import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


def get_user_remaning_time(user: AbstractUser):
    expired_time = datetime.timedelta(seconds=0)
    if not user.last_login:
        return expired_time
    now = timezone.now()
    expiration_time = user.last_login - now + settings.REST_FRAMEWORK_SUDO_EXPIRATION
    if expiration_time.total_seconds() < 0:
        return expired_time
    return expiration_time


def get_expires_at(user: AbstractUser):
    return timezone.now() + get_user_remaning_time(user)
