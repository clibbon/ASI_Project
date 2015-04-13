# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:06:16 2015

Functions for parsing text and saving it in django

@author: alex
"""

from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from lists import regions
import re
from nltk import pos_tag

class AppError(Exception):
    """ Class for all my errors from this app"""
    pass



def getTextInfo(message, debug=False):
    # Remove all non alpha numeric characters
    message = re.sub(r'([^\s\w]|_)+', '', message) 
        
    # Split the text up
    words = message.split()
    # Identify model no and serial no
    serNum, modelNum, words = findModelNums(words)
    # Find the region
    region = findRegion(message)
    # Remove non-Proper-nouns
    properNouns = selectProperNouns(words)
    # Remove any region matches
    words = removeRegions(words)
    # Find the names
    forename, surname = getNames(words)
    
    detailDict = {
    'ForeName' : forename,
    'SurName' : surname,
    'SerNo' : serNum,
    'ModNo' : modelNum,
    'Region': region
    }
    return detailDict

# Function adds details to the response cookie
def addDetailsToCookie(details,response):
    response.set_cookie("ForeName", value=details['ForeName'])
    response.set_cookie("SurName", value=details['SurName'])
    response.set_cookie("SerNo", value=details['SerNo'])
    response.set_cookie("ModNo", value=details['ModNo'])
    response.set_cookie("Region",value=details['Region'])
    return response

def getDetailsFromCookie(request):
    detailDict = {
    'ForeName' : request.COOKIES.get('ForeName',''),
    'SurName' : request.COOKIES.get('SurName',''),
    'SerNo' : request.COOKIES.get('SerNo',''),
    'ModNo' : request.COOKIES.get('ModNo',''),
    'Region': request.COOKIES.get('Region',0)
    }
    
    # Check that we've still got the cookie
    if detailDict['ForeName']=='':
        raise AppError(
        'Cookie has either timed out, or could not be '
        'loaded properly')
    return detailDict

def findModelNums(words):
    possibleMatches = [] 
    for word in words:
        if not re.match("^[A-Za-z]+$", word): 
            possibleMatches.append(word) 
    
    # Check for errors
    if len(possibleMatches) > 2:
        print possibleMatches
        raise AppError(
            'Could not identify serial number/model number,'
            ' too many alphanumeric words')
    elif len(possibleMatches) < 2:
        raise AppError(
            'To few serial number/model number '
            'matches found')
    
    # Find which is longest
    matchLengths = [len(i) for i in possibleMatches]
    
    # Check lengths aren't identical
    if matchLengths[0]==matchLengths[1]:
        raise AppError(
            'Could not distinguish serial number as same '
            'length as model num')
    
    # Get the index of the serial
    idx = matchLengths.index(max(matchLengths))
    
    serNum = possibleMatches.pop(idx)
    modelNum = possibleMatches[0]
    # Remove words from list
    words.remove(serNum)
    words.remove(modelNum)
    return (serNum, modelNum, words)

def getNames(properNouns):
    if len(properNouns) > 2:
        raise AppError('Too many names discovered')
    return properNouns[0],properNouns[1]
    
def findRegion(message):
    ratio = []
    # String match region names
    for region in regions:
        ratio.append(fuzz.partial_ratio(message,region))
    
    if max(ratio) > 80:
        idx = ratio.index(max(ratio))
    else:
        raise AppError('Could not identify a region')
    return regions[idx]

def selectProperNouns(words):
    properNouns = []
    taggedWords = pos_tag(words)
    for (word, type) in taggedWords:
        if type == 'NNP':
            properNouns.append(word)
    return properNouns
    
    
def removeRegions(words):
    newList = []
    for word in words:
        temp = []
        for region in regions:
            temp.append(fuzz.partial_ratio(word.lower(),
                                           region.lower()))
        if max(temp) < 90:
            newList.append(word)
    return newList
        
# Function extracts keywords from the message (it's the first word)
def getKeyWord(msgText):
    words = msgText.split()
    return words[0]

# Receipt on successful generation of new warranty
def generateConfirmationReply(pId, cId):
    return 'Warranty confirmed'
    
# Reponse to existing warranty
def existingWarrantyReply(pId, cId):
    return 'Warranty already exists'
    
