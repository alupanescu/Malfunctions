from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Malfunction


class MalfunctionCreateView(LoginRequiredMixin, CreateView):
    model = Malfunction
    template_name = "report_a_malfunction/index.html"
    fields = '__all__'
    success_url = reverse_lazy('homepage')
