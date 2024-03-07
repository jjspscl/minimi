from .models import Email

def get_emails():
    emails = Email.objects.all()
    return emails

def create_email_bulk(emails: list[str]):
    new_emails = []
    for email in emails:
        new_email = Email(content=email)
        new_emails.append(new_email)
    Email.objects.bulk_create(new_emails)
    return new_emails
