from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.utils.translation import get_language
from django.http.response import JsonResponse
from django.core.paginator import Paginator

from rest_framework.generics import ListAPIView

from .serializers import BranchenSerializer
from .models import Branchen, b

def index(request):
    # b_ids = Branchen.objects.values_list("b_id")
    # batch = [b(id=i[0]) for i in set(b_ids)]
    # print(batch)
    # b.objects.bulk_create(batch)

    return render(request, 'apps/main/home.html')


class BranchenApiView(ListAPIView):
    queryset = Branchen.objects.all()
    serializer_class = BranchenSerializer
    paginate_by = 20


    def get_queryset(self, **kwargs):
        letter = self.request.query_params.get('text_letter')
        branchen = Branchen.objects.filter(sprach__code__contains=get_language()).order_by('text')
        if letter and len(letter) == 1 and  "A" <= letter <= "Z":
            branchen = branchen.filter(text__startswith=letter)
        return branchen.all()


class BranchenView(TemplateView):
    template_name = "apps/main/branchen.html"

