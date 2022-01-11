from django.urls import path
from .views import CampRankView, OnlineRankView, StatusRankView

app_name = "home"

urlpatterns = [
    path("ranks/campaign/", CampRankView.as_view(), name="rank_campaign"),
    path("ranks/online/", OnlineRankView.as_view(), name="rank_online"),
    path("ranks/online/", StatusRankView.as_view(), name="rank_online"),
]
