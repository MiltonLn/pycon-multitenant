from django import forms

from tenants.models import Tenant


class TenantCreateForm(forms.ModelForm):
    subdomain = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Tenant
        fields = ['name', 'subdomain']

    def save(self, commit=True):
        instance = super().save(commit=False)
        subdomain = self.cleaned_data.get('subdomain')
        instance.schema_name = subdomain.replace('-', '_')
        # You need to replace localhost for your domain
        instance.domain_url = f'{subdomain}.localhost'
        instance.save()
        return instance
