from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .models import Tenant
from .forms import TenantCreateForm


class TenantsHome(TemplateView):
    template_name = 'tenants/tenants_home.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['tenants'] = Tenant.objects.exclude(schema_name='public')
        return context


class TenantCreateView(CreateView):
    form_class = TenantCreateForm
    model = Tenant
    template_name = 'tenants/tenant_form.html'
    success_url = reverse_lazy('home')
