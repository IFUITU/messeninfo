from django.shortcuts import render
from django.views.generic import ListView
from django.utils.translation import get_language

from .models import Branchen, b

def index(request):
    # b_ids = Branchen.objects.values_list("b_id")
    # batch = [b(id=i[0]) for i in set(b_ids)]
    # print(batch)
    # b.objects.bulk_create(batch)

    return render(request, 'apps/main/home.html')


class BranchenView(ListView):
    model = Branchen
    paginate_by = 20
    template_name = "apps/main/branchen.html"

    def get_queryset(self, **kwargs):
        branchen = Branchen.objects.filter(sprach__code__contains=get_language()).all()
        return branchen
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['branchen'] = Branchen.objects.all()
    #     return context