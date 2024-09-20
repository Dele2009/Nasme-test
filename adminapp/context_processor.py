from mainapp.models import Unit

def global_resources(request):
    all_units = Unit.objects.all()
    context = {
        'units': all_units
    }
    return context