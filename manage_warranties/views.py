from django.shortcuts import render
from django.http import HttpResponse
import twilio.twiml
from django_twilio.decorators import twilio_view
from text_funs import *
from db_funs import *
import sys
from django.views.generic.edit import CreateView
from manage_warranties.models import ProductSellers

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the index") 

# Test receiver.
@twilio_view
def test_bed(request):
    resp = twilio.twiml.Response()
    resp.message("Message received")
    return resp 

# Importer page
def importer_page(request):
    return HttpResponse("Welcome to the importers page")

# Main dashboard page
def information_page(request):
    return HttpResponse("Welcome to the information page")

# Test page for cookies
@twilio_view
def cookie_test(request):
    count = request.COOKIES.get('counter',0)
    print count
    resp = twilio.twiml.Response()
    print resp
    resp.message("There were " + str(count) + " messages")
    
    resp = HttpResponse(resp)
    resp.set_cookie("counter", value=str(int(count) + 1))
    
    return resp

# Demo day page - more robust and forwards message on to me
@twilio_view
def demo_day_receiver(request):

    return resp

# Main page for handling text messages
@twilio_view
def text_receiver(request):
    resp = twilio.twiml.Response()
    # Try to read the text and the sender
    try:
        msgText = request.POST.__getitem__('Body')
        msgSender = request.POST.__getitem__('From')
    except Exception as e:
        print e
    
    # Try to save the message
    try:
        saveMsgHistory(msgText, msgSender)
    except AppError as e:
        print e
        print 'Failed to save message'
    except Exception as e:
        print e
    
    # Check for keywords
    keyWord = getKeyWord(msgText)
    if keyWord == 'CORRECT':
        try:
            detailDict = getDetailsFromCookie(request)
            # Add to database
            warCreated, pId, cId = addToDatabase(detailDict,msgSender)
            if warCreated:
                resp.message(generateConfirmationReply(pId, cId))
            else:
                resp.message(existingWarrantyReply(pId, cId))
        except Exception as e:
            print e
            print sys.exc_traceback.tb_lineno
    else:
        # Parse the text
        try:
            details = getTextInfo(msgText)
        
            resp.message(generateSuccessReply(details))
            resp = HttpResponse(resp)
            # Store cookie
            resp = addDetailsToCookie(details,resp)
        except AppError as e:
            print e
            resp.message(
                        'Sorry your information could not be read. '
                        'Please enter it in this order: '
                        'Forename Surname SerialNo ModelNo Region')
        except Exception as e:
            print e
            
    print resp
    return resp

# Page for displaying received messages in a nice format
def message_table(request):
    messages = MessageHistory.objects.all()
    context = {'latest_question_list': messages}
    return render(request, 'Listener/message_table.html', context)

class CreateProductView(CreateView):
    
    model = ProductSellers
    template_name = 'add_importer.html'
    

# def test_input_page(request):