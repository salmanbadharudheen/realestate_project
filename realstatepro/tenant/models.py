

from django.db import models
from property.models import Unit

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    document_proofs = models.TextField()

    def __str__(self):
        return self.name

class RentalInformation(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.IntegerField()

    def __str__(self):
        return f"Rental Info for {self.tenant.name} in {self.unit.property.name}"
