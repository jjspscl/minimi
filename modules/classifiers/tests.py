from django.test import TestCase
from .ml_classifier import MLClassifier
from .logic_classifier import LogicClassifier
from apps.mail.models import Email


class MLClassifierTestCase(TestCase):
    def setUp():
        self.emails = [
            Email(content="Test Email Content 1"),
            Email(content="Test Email Content 2"),
            Email(content="Test Email Content 3"),
            Email(content="Test Email Content 4"),
            Email(content="Test Email Content 5"),
        ]

        
    def test_train(self):
        classifier = MLClassifier()
        classifier.train()
        self.assertTrue(classifier.trained_model)



class LogicClassifierTestCase(TestCase):
    def setUp(self):
        self.keywords = ['unsubscribe']
        self.default = 'regular'
        self.emails = [
            Email(content=f'Test Email Content {"unsubscribe" if i % 2 == 0 else "regular"}') for i in range(1, 1000)
        ]

    def test_classify(self):
        classifier = LogicClassifier(
            emails=self.emails,
            keywords=self.keywords,
            default=self.default
        )
        data = classifier.classify()
        
        self.assertEqual(data[0][1], 'unsubscribe')
        self.assertEqual(data[1][1], 'regular')
        self.assertEqual(data[2][1], 'unsubscribe')