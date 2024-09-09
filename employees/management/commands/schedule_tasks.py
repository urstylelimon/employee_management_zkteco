# employees/management/commands/schedule_tasks.py
from django.core.management.base import BaseCommand
from django_q.tasks import schedule

class Command(BaseCommand):
    help = 'Schedule daily tasks'

    def handle(self, *args, **kwargs):
        # Schedule the task to run daily
        schedule(
            'employees.tasks.check_and_remove_expired_employees',
            schedule_type='D'
        )
        self.stdout.write(self.style.SUCCESS('Daily task scheduled.'))
