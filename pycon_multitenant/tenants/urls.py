from django.urls import path

from . import views


app_name = 'tenants'

urlpatterns = [
    path('create/', views.TenantCreateView.as_view(), name='create')
]
