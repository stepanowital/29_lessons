import os

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Loads fixtures from fixtures dir"
    fixtures_dir = "fixtures"
    loaddata_command = "loaddata"
    filenames = [
        "list_view",
        "retrieve_view",
        "slug_retrieve_view",
        "update_view",
        "simple_serializer",
        "fk_serializer",
        "m2m_serializer"
    ]

    def handle(self, *args, **options):
        for fixture_filename in self.filenames:
            call_command(
                self.loaddata_command, os.path.join(self.fixtures_dir, f"{fixture_filename}.json")
            )
