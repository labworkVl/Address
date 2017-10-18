from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Successfully created {0} tags!'.format(100))
