"""
django command  for wait for the db to be aviable for the user
sometime the app start it before the db, so to avoid error,
we sleep 1 second everytime the app fail to connect to the db
"""

import time
from psycopg2 import OperationalError as Pysopg20pError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """django commant to wait for db"""

    def handle(self, *args, **options):
        """entrypoint for commands"""
        self.stdout.write("waiting for db....")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Pysopg20pError, OperationalError):
                self.stdout.write("datatabse unavaible, waiting 1 second ")
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('database is ready!!!!!'))
