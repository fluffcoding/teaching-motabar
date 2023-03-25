from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()



class Report(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField(null=True, blank=True)


    def __str__(self):
        return f'{self.id} - {self.name} - {self.user.username}'