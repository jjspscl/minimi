from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from modules.email_source import csv_reader
from .services import create_email_bulk
from .models import Email

def upload_csv(request):
    if request.htmx:
        if 'csv_file' in request.FILES:
            if request.FILES['csv_file'].content_type != 'text/csv':
                return HttpResponse('Invalid file type')

            csv_file = request.FILES['csv_file']
            csv_data = csv_reader.process_csv(csv_file)

            create_email_bulk(csv_data)
            
            return HttpResponse('File uploaded successfully')
        else:
            return HttpResponse('No file uploaded')
    
    if request.method == 'GET':
        return render(request, 'mail/upload_csv.html')

def email_table(request):
    # if request.htmx:
    #     emails = sync_to_async(get_emails)()
    #     return render(request, 'mail/email_view.html', {'emails': emails})

    page_number = request.GET.get('page', 1)
    paginator = Paginator(Email.objects.all(), 5)
    email_obj = paginator.get_page(page_number)

    print(email_obj.has_next())
    return render(request, 'mail/email_table.html', {'email_obj': email_obj })
