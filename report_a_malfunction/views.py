from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .forms import MalfunctionUpdateForm
from .models import Malfunction


class MalfunctionCreateView(LoginRequiredMixin, CreateView):
    model = Malfunction
    template_name = "report_a_malfunction/index.html"
    fields = '__all__'
    success_url = reverse_lazy('malfunctions-status')

class MalfunctionListView(ListView):
    model = Malfunction
    template_name = "report_a_malfunction/malfunctions_status.html"
    context_object_name = "all_malfunctions"
    fields = '__all__'





class MalfunctionUpdateView(UpdateView):
    template_name = "report_a_malfunction/update_malfunctions.html"
    model = Malfunction
    form_class = MalfunctionUpdateForm
    success_url = reverse_lazy('malfunctions-status')


class MalfunctionDeleteView(DeleteView):
    template_name = 'report_a_malfunction/delete_malfunctions.html'
    model = Malfunction
    success_url = reverse_lazy('malfunctions-status')

def search(request):
    get_value = request.GET.get('search')
    get_data = Malfunction.objects.filter(name__icontains=get_value)
    context = {'all_malfunctions': get_data}
    return render(request, 'report_a_malfunction/search.html', context)
