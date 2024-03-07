from django.test import TestCase
from .models import MLModel
from . import services

class ClassifierServiceTestCase(TestCase):
    def test_get_ml_models(self):
        ml_model = MLModel.objects.create(name="Test Model", model_file="test_model.pkl")
        self.assertEqual(services.get_ml_models()[0].name, "Test Model")
    
    def test_create_ml_model(self):
        ml_model = services.create_ml_model("Test Model", "test_model.pkl")
        self.assertEqual(MLModel.objects.get(pk=ml_model.pk).name, "Test Model")

    def test_update_ml_model(self):
        ml_model = MLModel.objects.create(name="Test Model", model_file="test_model.pkl")
        updated_ml_model = services.update_ml_model(ml_model.pk, "Updated Model", "updated_model.pkl")
        self.assertEqual(MLModel.objects.get(pk=updated_ml_model.pk).name, "Updated Model")


    def test_delete_ml_model(self):
        ml_model = MLModel.objects.create(name="Test Model", model_file="test_model.pkl")
        deleted_ml_model = services.delete_ml_model(ml_model.pk)
        with self.assertRaises(MLModel.DoesNotExist):
            MLModel.objects.get(pk=deleted_ml_model.pk)

    def test_create_ml_model_bulk(self):
        models = [
            {"name": "Test Model 1", "model_file": "test_model_1.pkl"},
            {"name": "Test Model 2", "model_file": "test_model_2.pkl"},
            {"name": "Test Model 3", "model_file": "test_model_3.pkl"},
            {"name": "Test Model 4", "model_file": "test_model_4.pkl"},
            {"name": "Test Model 5", "model_file": "test_model_5.pkl"},
        ]
        new_models = services.create_ml_model_bulk(models)
        for model in new_models:
            self.assertEqual(MLModel.objects.get(pk=model.pk).name, model.name)
        self.assertEqual(len(new_models), len(models))