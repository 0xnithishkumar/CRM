from django.db import models
from datetime import datetime

class Customer_db(models.Model):
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    updated_on = models.DateTimeField(default=datetime.now, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    