from django.db import models
from Accounts.models import User
from Project.models import Projecto

    # Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
         ('PENDING', 'Pending'),
         ('IN_PROGRESS', 'In Progress'),
         ('COMPLETED', 'Completed'),
         ('REJECTED', 'Rejected'),
    ]

    name = models.CharField(max_length=255)
    project = models.ForeignKey(Projecto, on_delete=models.CASCADE)
    # assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,  default='PENDING')
    premisses_Locked = models.IntegerField(blank=True,default=0 )
    meter_box = models.IntegerField(blank=True, default=0)
    acess_denied = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}-{self.name}'
    
