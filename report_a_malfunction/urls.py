from django.contrib import admin
from django.urls import path, include

from report_a_malfunction.views import MalfunctionCreateView, MalfunctionListView

# from .views import index, MalfunctionCreateView

urlpatterns = [
    path("", MalfunctionCreateView.as_view(), name="malfunction-index"),
    path("malfunctions_status/", MalfunctionListView.as_view(), name="malfunctions-status"),
]