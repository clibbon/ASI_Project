# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:46:08 2015

@author: alex

Functions for saving the data to the database in django,
 and creating the reply message.
"""

from datetime import datetime
from manage_warranties.models import MessageHistory

def saveMsgHistory(message, sender):
    MessageHistory.objects.create(msg_text = message, 
                                  date_received = datetime.now().date(), \
                                  mob_number = sender)

def saveMessageInfo(details, sender, message):
    ''' Details is a tuple containing (serNum, modelNum, region, 
    forename, surname), and sender is a string of the sender number
    '''
    print details[3]
    print details[4]
    # Save to the message history    
    
                        
def generateSuccessReply(details):
    detailDict = {
    'FName' : details[3],
    'SName' : details[4],
    'SerNo' : details[0],
    'ModNo' : details[1],
    'Region': details[2]
    }
    
    msgText = ('''Thankyou for registering. Your details are 
    Name %(FName)s %(SName)s,
    SerNo %(SerNo)s, Model %(ModNo)s, Region %(Region)s.
    If this is incorrect reply with the word
    RETRY''' % detailDict)
    return msgText
    
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

