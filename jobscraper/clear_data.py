from django.db import transaction
from jobscraper.models import ScrapedData

with transaction.atomic():
    ScrapedData.objects.all().delete()

# python manage.py shell
# exec(open('jobscraper/clear_data.py').read())
