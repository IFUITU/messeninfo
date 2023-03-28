from django.urls import path
from .views import index, BranchenApiView, BranchenView

api_urls = [
    path("api/get-branchens/", BranchenApiView.as_view(), name="branchen_get"),

]

urlpatterns = [
    path("", index, name="home"),
    path("branchen/", BranchenView.as_view(), name="branchen"),

] + api_urls

