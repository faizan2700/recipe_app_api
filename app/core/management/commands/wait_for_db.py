""" 
Wait for database to be available 
""" 
import time 
from psycopg2 import OperationalError as Psycopg2Error 

from django.db.utils import OperationalError 
from django.core.management.base import BaseCommand 


class Command(BaseCommand): 
    """ 
    Django command to wait for database.  
    """
    def handle(self, *args, **options):
        """ 
        Entry point for command 
        """
        self.stdout.write('Waiting for database...') 
        db_up = False 
        while not db_up: 
            try: 
                db_up = self.check(databases=['default']) 
            except (Psycopg2Error, OperationalError): 
                self.stdout.write('Database unavailable waiting one second...') 
                time.sleep(1) 
        self.stdout.write(self.style.SUCCESS('Databases available!'))  

    def check(self, databases=None): 
        return True 
