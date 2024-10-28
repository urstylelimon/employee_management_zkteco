# employees/models.py
from django.db import models
from datetime import date

class Employee(models.Model):
    # Adding UN Road and Park Road in addition to Road 1 to Road 14
    ROAD_CHOICES = [(f"Road {i}", f"Road {i}") for i in range(1, 15)] + [
        ("UN Road", "UN Road"),
        ("Park Road", "Park Road")
    ]

    name = models.CharField(max_length=100)
    rfid_card = models.BigIntegerField(unique=True)
    job_description = models.CharField(max_length=100)
    road_number = models.CharField(max_length=10, choices=ROAD_CHOICES)  # Dropdown for road numbers
    house_number = models.CharField(max_length=10)  # Text field for house number
    expire_date = models.DateField()
    is_active = models.BooleanField(default=True)
    added_to_machine = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.rfid_card}) - {self.road_number}, House {self.house_number}"

    def check_expiration(self):
        """Automatically marks the employee inactive if expired."""
        if date.today() > self.expire_date and self.is_active:
            self.is_active = False
            self.save(update_fields=['is_active'])
