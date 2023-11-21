from django.core.mail import send_mail, BadHeaderError
from jobscraper.models import ScrapedData
import uuid

def send_otp(email, otp):
    subject = 'Your OTP for Verification'
    message = f"Your OTP is: {otp}"
    from_email = 'manishsalavkar78@gmail.com'
    recipient_list = [email]
    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return True
    except BadHeaderError:
        print("Invalid header found")
    except Exception as e:
        print(f"Error sending OTP: {str(e)}")


def generate_jobid():
    while True:
        jobid = str(uuid.uuid4()).replace("-", "")[:16]
        if jobid not in ScrapedData.objects.values_list('jobid', flat=True):
            return jobid
        

def extract_form_data(form):
    job_title = form.cleaned_data['job_title']
    location = form.cleaned_data['location']
    job_types = form.cleaned_data['job_type']
    min_salary = form.cleaned_data['min_salary']
    max_salary = form.cleaned_data['max_salary']
    salary_unit = form.cleaned_data['salary_unit']
    job_description = form.cleaned_data['job_description']

    return job_title, location, job_types, min_salary, max_salary, salary_unit, job_description