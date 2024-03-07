from django.shortcuts import render
from django.http import HttpResponse
from apps.mail.models import Email
from modules.paginator import is_htmx, paginate
from modules.classifiers.logic_classifier import LogicClassifier
from modules.classifiers.ml_classifier import MLClassifier

def logic_classifier(request):
    if is_htmx(request):
        mails = Email.objects.all()

        classifier = LogicClassifier(
            emails=mails,
            keywords=['unsubscribe'],
            default='regular'
        )
        results = classifier.classify()


        data = paginate(request, results, limit=5)
        page = request.GET.get('page', 1)
        return render(request, "classifier/logic/result.html", {'results': data })
    elif request.method == "GET":
        return render(request, 'classifier/logic/classifier.html')

def ml_train(request):
    if is_htmx(request):
        mails = Email.objects.all()

        classifier = MLClassifier(mails)
        classifier.train()

        return HttpResponse("Model trained")

        
    elif request.method == "GET":
        return render(request, 'classifier/ml/train.html')
    
def ml_predict(request):
    if is_htmx(request):
        pass
    elif request.method == "GET":
        return render(request, 'classifier/ml/predict.html')