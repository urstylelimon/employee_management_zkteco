# employees/models.py
from django.db import models
from datetime import date

class Employee(models.Model):
    name = models.CharField(max_length=100)
    rfid_card = models.CharField(max_length=50, unique=True)
    job_description = models.CharField(max_length=100)
    expire_date = models.DateField()
    is_active = models.BooleanField(default=True)
    added_to_machine = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.rfid_card})"

    # Mark employee inactive after expiration
    def check_expiration(self):
        if date.today() > self.expire_date:
            self.is_active = False
            self.save()
