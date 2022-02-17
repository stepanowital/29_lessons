import os

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Loads fixtures from fixtures dir"
    fixtures_dir = "fixtures"
    loaddata_command = "loaddata"
    filenames = [
        "router",
        "lookup_queries",
        "lookup_queries_2",
        "lookup_queries_3",
        "qf_queries",
        # "qf_queries_2",
        "fk_search",
        "delete_if_null"
    ]

    def handle(self, *args, **options):
        for fixture_filename in self.filenames:
            call_command(
                self.loaddata_command, os.path.join(self.fixtures_dir, f"{fixture_filename}.json")
            )
