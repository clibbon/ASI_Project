# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:46:08 2015

@author: alex

Functions for saving the data to the database in django,
 and creating the reply message.
"""

from datetime import datetime
from manage_warranties.models import MessageHistory, Customers, Products

# Function to save incoming message to msg log
def saveMsgHistory(message, sender):
    MessageHistory.objects.create(msg_text = message, 
                                  date_received = datetime.now().date(), \
                                  mob_number = sender)  

                        
# Function to generate a response
def generateSuccessReply(detailDict):
    
    msgText = (
        'Thankyou for registering. Your details are: '
        'Name - %(ForeName)s %(SurName)s, \n'
        'SerNo -  %(SerNo)s, \n' 
        'Model %(ModNo)s, \n'
        'Region %(Region)s. \n'
        'If this is incorrect reply with the word RETRY'
        % detailDict)
    return msgText
    
# Function checks if a customer exists, and if not creates one
def checkCustomer(detailDict,mob_num):
    c = Customers.objects.get_or_create(
        first_name = detailDict['ForeName'],
        last_name = detailDict['SurName'],
        mob_number = mob_num,
        region = detailDict['Region']
        )
        
    return c.cId
    
# Function checks if a product exists
def checkProduct(detailDict):
    p = Products.objects.get_or_create(
        ser_num = detailDict['SerNum'],
        model = detailDict['Model']
        )
    return p.pId

# Function checks if a warranty exists
def warrantyExists(cId,pId):
    warranties.objects.get(
        cId = cId,pId = pId
        ).exists()

# Function attempts to add warranty to the database
def addToDatabase(details):
    '''Function will return True if successful
    otherwise will return false'''
    
    # Check if customer and/or warranty already exist
    cId = checkCustomer(detailDict,mob_num)
    pId = checkProduct(detailDict)
    
    # Check if a warranty exists already
    if warrantyExists(cId,pId):
       return False
    else:
        createWarranty(detailDict,cId,pId,mob_num)
        return True

    
    


    '''
    # First customer
    try:
        c = Customer.objects.get(first_name = details[3], \
        last_name = details[4])
    except Customer.DoesNotExist:
        c = Customer.objects.create(first_name = details[3], \
        last_name = details[4])
    Customer.objects.create
    '''

