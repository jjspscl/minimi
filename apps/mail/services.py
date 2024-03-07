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

def create_email(content: str):
    email = Email(content=content)
    email.save()
    return email

def update_email(email_id: int, content: str):
    email = Email.objects.get(pk=email_id)
    email.content = content
    email.save()
    return email

def delete_email(email_id: int):
    email = Email.objects.get(pk=email_id)
    email.delete()
    return email
