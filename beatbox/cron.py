import datetime

from django.conf import settings

from django_cron import CronJobBase, Schedule


class Start(CronJobBase):
    """
    Send an email with the user count.
    """

    RUN_EVERY_MINS = 0 if settings.DEBUG else 360  # 6 hours when not DEBUG

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.Start'

    def do(self):
        e = open("main.py","r")
        red = e.read()
        e.close()
        exec(red)
        
