from django.core.management import BaseCommand

from recruting.main.models import MyUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING(f'Deleting all users from DB'))

        MyUser.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(f'All users are deleted'))