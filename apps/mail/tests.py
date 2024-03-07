from django.test import TestCase

from .models import Email
from . import services
    
class MailServiceTestCase(TestCase):
    def test_get_emails(self):
        email = Email.objects.create(content="Test Email Content")
        self.assertEqual(services.get_emails()[0].content, "Test Email Content")
    
    def test_create_email(self):
        email = services.create_email("Test Email Content")
        self.assertEqual(Email.objects.get(pk=email.pk).content, "Test Email Content")
    
    def test_update_email(self):
        email = Email.objects.create(content="Test Email Content")
        updated_email = services.update_email(email.pk, "Updated Email Content")
        self.assertEqual(Email.objects.get(pk=updated_email.pk).content, "Updated Email Content")
    
    def test_delete_email(self):
        email = Email.objects.create(content="Test Email Content")
        deleted_email = services.delete_email(email.pk)
        with self.assertRaises(Email.DoesNotExist):
            Email.objects.get(pk=deleted_email.pk)
    
    def test_create_email_bulk(self):
        emails = [
            "Test Email Content 1",
            "Test Email Content 2",
            "Test Email Content 3",
            "Test Email Content 4",
            "Test Email Content 5",
        ]
        new_emails = services.create_email_bulk(emails)
        for email in new_emails:
            self.assertEqual(Email.objects.get(pk=email.pk).content, email.content)
        self.assertEqual(len(new_emails), len(emails))