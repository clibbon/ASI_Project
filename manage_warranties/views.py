from django.shortcuts import render
from django.http import HttpResponse
import twilio.twiml
from django_twilio.decorators import twilio_view

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the index") 

def importer_page(request):
    return HttpResponse("Welcome to the importers page")

def information_page(request):
    return HttpResponse("Welcome to the information page")

@twilio_view
def text_receiver(request):
    resp = twilio.twiml.Response()
    resp.message("A successful response")
    
    temp = Message(msg_text = request.body)
    temp.save()
    return resp

def message_table(request):
    messages = Message.objects.all()
    context = {'latest_question_list': messages}
    return render(request, 'Listener/message_table.html', context)