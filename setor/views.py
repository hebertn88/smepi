from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Setor


# Create your views here.
def setores(request):
    context = {
        'setores' : Setor.objects.all()}
    return render(request, 'setor/setores.html', context)


def edit_setor(request, id):
    setor = get_object_or_404(Setor, pk=id)
    return HttpResponse(f'{setor.id}, {setor.descricao}')