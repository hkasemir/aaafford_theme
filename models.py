from django.db import models

class UserProfile(models.Model):
  user = models.OneToOneField("auth.User")
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  phone_number = models.CharField(max_length=20)
  member_since = models.DateTimeField(auto_now_add=True, blank=True)
  units = models.TextField()
