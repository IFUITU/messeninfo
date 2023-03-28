from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.utils.translation import get_language
from django.http.response import JsonResponse
from django.core.paginator import Paginator



def index(request):
    # b_ids = Branchen.objects.values_list("b_id")
    # batch = [b(id=i[0]) for i in set(b_ids)]
    # print(batch)
    # b.objects.bulk_create(batch)

    return render(request, 'apps/main/home.html')

class BranchenView(TemplateView):
    template_name = "apps/main/branchen.html"

