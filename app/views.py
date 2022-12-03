from django.shortcuts import render
from django.http import HttpResponse


def app(request):
    return render(request, 'index.html', {})

def send(request):
    print("Done !!!")
    return HttpResponse('Message sent successfully')





#######----------------------#######


#######----------------------#######
