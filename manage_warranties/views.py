from django.shortcuts import render
from django.http import HttpResponse
import twilio.twiml
from django_twilio.decorators import twilio_view
from text_funs import *
from db_funs import *
import os

# Create your views here.
def index(request):
    print(os.listdir('.'))
    return HttpResponse("Welcome to the index") 

def importer_page(request):
    return HttpResponse("Welcome to the importers page")

def information_page(request):
    return HttpResponse("Welcome to the information page")

@twilio_view
def text_receiver(request):
    resp = twilio.twiml.Response()
    msgText = request.POST.__getitem__('Body')
    msgSender = request.POST.__getitem__('From')
    saveMsgHistory(msgText, msgSender)
    
    # See if we can parse information
    try: 
        details = getTextInfo(msgText) # Details is a tuple containing (serNum, modelNum, region, forename, surname)
        resp.message(generateSuccessReply(details))
    except AppError:
        resp.message('Sorry your information could not be read. Please enter it \
        in this order Forename Surname SerialNo ModelNo Region')
    
    
    resp.message('Message received')
    
    # Save the information
    #temp = MessageHistory(msg_text = request.Body)
    #temp.save()
    
   
    return resp #HttpResponse(yourMsg + ' from ' + whoDidIt)

def message_table(request):
    messages = MessageHistory.objects.all()
    context = {'latest_question_list': messages}
    return render(request, 'Listener/message_table.html', context)

def message_history(request):
    messages = MessageHistory.objects.all()
    return HttpResponse("")
