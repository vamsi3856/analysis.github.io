from django.shortcuts import render

# Create your views here.
import csv, io
from django.shortcuts import render
from django.contrib import messages
from sheetapp.models import *
# Create your views here.
# one parameter named request
def profile_upload(request):
    # declaring template
    template = "profile_upload.html"
    
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
           
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        print(column)
        machine=Machine.objects.get(machine_no=column[0])
        print(machine,column[1])    
        processes = Process.objects.get(machine=machine,process_name=column[1])
        
        _, created = Productdetail.objects.update_or_create(
            machine=machine,
            process=processes,
            starttime=column[2],
            endtime=column[3]
        )
        print(_,created)
        
    context = {}
    return render(request, template, context)