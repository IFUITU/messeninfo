from rest_framework.generics import ListAPIView
from django.utils.translation import get_language

from .serializers import BranchenSerializer
from .models import Branchen, b

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
