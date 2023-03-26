from django.shortcuts import render
from .models import Branchen, b
# Create your views here.

def index(request):
    b_ids = Branchen.objects.values_list("b_id")
    batch = [b(id=i[0]) for i in set(b_ids)]
    print(batch)
    b.objects.bulk_create(batch)
        

    return render(request, 'apps/main/home.html')