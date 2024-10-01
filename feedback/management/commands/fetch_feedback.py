from django.core.management.base import BaseCommand
import pandas as pd
from feedback.models import Feedback  # Replace 'feedback' with your actual app name

class Command(BaseCommand):
    help = 'Fetch feedback data and save to CSV'

    def handle(self, *args, **kwargs):
        feedback_records = Feedback.objects.all().values()
        feedback_df = pd.DataFrame(list(feedback_records))
        feedback_df.to_csv('feedback_from_django.csv', index=False)
        self.stdout.write(self.style.SUCCESS('Successfully fetched feedback data'))
