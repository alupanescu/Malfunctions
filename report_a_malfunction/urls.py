

from django.contrib import admin
from django.urls import path, include

from report_a_malfunction import views
from report_a_malfunction.views import MalfunctionCreateView, MalfunctionListView, MalfunctionUpdateView, \
    MalfunctionDeleteView

# from .views import index, MalfunctionCreateView

urlpatterns = [
    path("", MalfunctionCreateView.as_view(), name="malfunction-index"),
    path("malfunctions_status/", MalfunctionListView.as_view(), name="malfunctions-status"),
    path("update_malfunctions/<int:pk>/", MalfunctionUpdateView.as_view(), name="update-malfunctions"),
    path("delete_malfunctions/<int:pk>/", MalfunctionDeleteView.as_view(), name="delete-malfunctions"),
    path('search/', views.search, name='search') # import?
]