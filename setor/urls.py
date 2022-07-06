from django.urls import path
from setor.views import SetorCreateView, SetorListView


urlpatterns = [
    path('', SetorListView.as_view(), name='setor_list'),
    path('create/', SetorCreateView.as_view(), name='setor_create'),

    #path('<int:id>/', views.edit_setor, name='edit_setor'),
    ]
