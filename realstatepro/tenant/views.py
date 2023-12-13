
from django.shortcuts import render
from .models import Tenant, RentalInformation

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_list.html', {'tenants': tenants})

def tenant_detail(request, tenant_id):
    tenant_instance = Tenant.objects.get(id=tenant_id)
    rental_info = tenant_instance.rentalinformation_set.all()
    return render(request, 'tenant_detail.html', {'tenant': tenant_instance, 'rental_info': rental_info})
