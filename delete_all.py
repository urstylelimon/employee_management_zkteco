from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Deletes all data from all tables in the SQLite database'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            # Get a list of all tables in the database
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

            # Delete all data from each table
            for table in tables:
                table_name = table[0]
                if table_name != 'sqlite_sequence':  # Skip the sqlite_sequence table
                    cursor.execute(f"DELETE FROM {table_name};")
                    self.stdout.write(self.style.SUCCESS(f'Successfully deleted all data from {table_name}'))

        self.stdout.write(self.style.SUCCESS('All data has been deleted from all tables.'))
print("Successfully deleted all data from all tables.")