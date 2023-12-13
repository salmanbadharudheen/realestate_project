from django.shortcuts import render


from django.shortcuts import render
from .models import Property, Unit
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def property_detail(request, property_id):
    property_instance = Property.objects.get(id=property_id)
    units = property_instance.unit_set.all()
    return render(request, 'property_detail.html', {'property': property_instance, 'units': units})
