
from .models import MLModel

def get_ml_models():
    ml_models = MLModel.objects.all()
    return ml_models

def create_ml_model(name: str, model_file: str):
    ml_model = MLModel(name=name, model_file=model_file)
    ml_model.save()
    return ml_model

def get_or_create_ml_model(name: str):
    ml_model, created = MLModel.objects.get_or_create(name=name)
    return ml_model, created


def update_ml_model(pk: int, name: str, model_file: str):
    ml_model = MLModel.objects.get(pk=pk)
    ml_model.name = name
    ml_model.model_file = model_file
    ml_model.save()
    return ml_model

def delete_ml_model(pk: int):
    ml_model = MLModel.objects.get(pk=pk)
    ml_model.delete()
    return ml_model

def create_ml_model_bulk(models: list[dict]):
    new_models = []
    for model in models:
        new_model = MLModel(name=model["name"], model_file=model["model_file"])
        new_models.append(new_model)
    MLModel.objects.bulk_create(new_models)
    return new_models