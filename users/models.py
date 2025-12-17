from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    last_seen = models.DateTimeField(default=timezone.now)
    
    def get_status(self):
        from django.utils import timezone
        import datetime
        
        time_diff = timezone.now() - self.last_seen
        return 'online' if time_diff.total_seconds() < 300 else 'offline'

    def __str__(self):
        return self.username