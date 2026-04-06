from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    passengers = models.CharField(max_length=20)
    from_location = models.CharField(max_length=200)
    to_location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name