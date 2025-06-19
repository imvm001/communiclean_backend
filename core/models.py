from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}({self.location})"

class ServiceBooking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} at {self.timestamp}"

class Income(models.Model):
    service = models.ForeignKey(ServiceBooking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    recorded_at = models.DateTimeField(auto_now_add=True)

class TaxRecord(models.Model):
    income = models.ForeignKey(Income, on_delete=models.CASCADE)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    recorded_at = models.DateTimeField(auto_now_add=True)



   
