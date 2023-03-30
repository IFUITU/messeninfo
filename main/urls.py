from django.urls import path
from .views import index, BranchenView, MessenView
from .api import BranchenApiView, BtomApiView

app_name = 'main'

api_urls = [
    path("api/get-branchens/", BranchenApiView.as_view(), name="branchen_get"),
    path("api/get-messe/<int:b_id>/", BtomApiView.as_view(), name="messe-get"),
]

urlpatterns = [
    path("", index, name="home"),
    path("branchen/", BranchenView.as_view(), name="branchen"),
    path("messe/<int:b_id>/", MessenView.as_view(), name='messe'),

] + api_urls

