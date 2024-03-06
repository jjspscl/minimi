from django.shortcuts import render
from django.http import HttpResponse
from modules.email_source import csv_reader

def upload_csv(request):
    if request.htmx:
        if 'csv_file' in request.FILES:
            if request.FILES['csv_file'].content_type != 'text/csv':
                return HttpResponse('Invalid file type')

            csv_file = request.FILES['csv_file']
            csv_data = csv_reader.process_csv(csv_file)

            for data in csv_data:
                print(data, end='\n-ENDD\n\n')
            return HttpResponse('File uploaded successfully')
        else:
            return HttpResponse('No file uploaded')
    
    if request.method == 'GET':
        return render(request, 'mail/upload_csv.html')
