from django.urls import path
from . import views


urlpatterns = [
    path('', views.setores, name='setores'),
    path('<int:id>/', views.edit_setor, name='edit_setor'),
    ]
