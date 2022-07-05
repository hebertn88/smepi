from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Setor
from .forms import SetorEditForm

# Create your views here.
def setores(request):
    context = {
        'setores' : Setor.objects.all()}
    return render(request, 'setor/setores.html', context)


def edit_setor(request, id):
    setor = get_object_or_404(Setor, pk=id)
    form = SetorEditForm(instance=setor)

    context = {'form': form, 'setor' : setor}

    return render(request, 'setor/edit-setor.html', context)