from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.get_risk_type, name='get_risk_type'),
    path('', views.get_risk_types, name='get_risk_types')
]