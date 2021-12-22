from django.urls import path
from .views import cadastrar_despesa

urlpatterns = [
    path('despesa/', cadastrar_despesa, name="despesa"),
]
