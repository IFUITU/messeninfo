from django.urls import path
from .views import index, BranchenView

urlpatterns = [
    path("", index, name="home"),
    path("branchen/", BranchenView.as_view(), name="branchen"),
    
]