from django.core.management.base import BaseCommand, CommandError
from tenants.models import Tenant


class Command(BaseCommand):
    help = 'Creates the public tenant record for the project'

    def handle(self, **kwargs):
        public_tenant, created = Tenant.objects.get_or_create(
            # It should be your project domain, maybe you need to add it to
            # settings to handle your different project instances
            domain_url='localhost',
            schema_name='public',
            # Whatever you want
            name='Public Tenant',
            # ...Your required fields for your Tenant model
        )
        if created:
            success_message = self.style.SUCCESS(
                'Successfully created public tenant!'
            )
            self.stdout.write(success_message)
        else:
            raise CommandError('Public tenant is already created')