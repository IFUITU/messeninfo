from rest_framework.generics import ListAPIView
from django.utils.translation import get_language
from rest_framework.pagination import PageNumberPagination

from .serializers import BranchenSerializer, BtomSerializer, MesseSerializer
from .models import Branchen, b, Messe, Btom



class BranchenApiView(ListAPIView):
    queryset = Branchen.objects.all()
    serializer_class = BranchenSerializer
    # paginate_by = 20


    def get_queryset(self, **kwargs):
        letter = self.request.query_params.get('text_letter')
        branchen = Branchen.objects.filter(sprach__code__contains=get_language()).order_by('text')
        
        if letter:
            if len(letter) == 1 and  "A" <= letter <= "Z":
                branchen = branchen.filter(text__startswith=letter)
            elif letter == '0-9':
                branchen = branchen.filter(text__regex = '\d+')
                print(branchen)
        return branchen.all()


class BtomApiView(ListAPIView):
    queryset = Btom.objects.all()
    serializer_class = BtomSerializer
    # paginate_by = 20
 

    def get_queryset(self, **kwargs):
        b_id = self.kwargs['b_id']
        print(b_id)
        messes = Btom.objects.filter(b_id=b_id)#.values_list("b_id", "messe__messe_logo")
        return messes.all()