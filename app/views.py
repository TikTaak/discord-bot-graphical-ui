from django.shortcuts import render
from django.http import HttpResponse

from discord_bot.bot import run_bot

def app(request):
    return render(request, 'index.html', {})

def send(request):
    run_bot()
    print("Done !!!")
    return HttpResponse('Message sent successfully')
    


print("haaaayaaa")

#######----------------------#######


#######----------------------#######
