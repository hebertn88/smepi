from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Setor
from .forms import SetorEditForm

# Create your views here.

class SetorCreateView(CreateView):
    model = Setor
    fields = ['descricao']

class SetorListView(ListView):
    model = Setor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def edit_setor(request, id):
    setor = get_object_or_404(Setor, pk=id)
    form = SetorEditForm(instance=setor)

    context = {'form': form, 'setor' : setor}

    return render(request, 'setor/edit-setor.html', context)