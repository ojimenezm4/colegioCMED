from django.shortcuts import render, redirect, get_object_or_404
from .models import Ciclo
from .forms import CicloForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class CicloListView(ListView):
    model = Ciclo
    template_name = 'ciclo/ciclo_list.html'
    context_object_name = 'ciclos'

class CicloCreateView(CreateView):
    model = Ciclo
    form_class = CicloForm
    template_name = 'ciclo/ciclo_form.html'
    success_url = '/ciclo/list/'

class CicloUpdateView(UpdateView):
    model = Ciclo
    form_class = CicloForm
    template_name = 'ciclo/ciclo_form.html'
    success_url = '/ciclo/list/'

class CicloDeleteView(DeleteView):
    model = Ciclo
    template_name = 'ciclo/ciclo_confirm_delete.html'
    success_url = '/ciclo/list/'

def ciclo_detail(request, pk):
    ciclo = get_object_or_404(Ciclo, pk=pk)
    return render(request, 'ciclo/ciclo_detail.html', {'ciclo': ciclo})