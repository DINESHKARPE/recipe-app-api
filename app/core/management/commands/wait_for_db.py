import time

from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Djnago commnad to pause execution until database is available """
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connection['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 Second')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))

