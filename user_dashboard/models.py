from django.db import models
from django.contrib.auth.models import User


class ContactAdmin(models.Model):
    """
    Contact admin model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
