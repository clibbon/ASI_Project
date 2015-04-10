# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:46:08 2015

@author: alex

Functions for saving the data to the database in django,
 and creating the reply message.
"""

from datetime import datetime
from manage_warranties.models import MessageHistory, Customers

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
    
def checkCustomer(detailDict,mob_num):
    c = Customers.objects.get_or_create(
        first_name = detailDict['ForeName'],
        last_name = detailDict['SurName'],
        mob_number = mob_num,
        region = detailDict['Region']
        )
    return c

def addToDatabase():
    pass


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

