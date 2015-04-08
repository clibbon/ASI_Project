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



def getTextInfo(message):
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
    
    return (serNum, modelNum, region, forename, surname)

def findModelNums(words):
    possibleMatches = [] 
    for word in words:
        if not re.match("^[A-Za-z]+$", word): 
            possibleMatches.append(word) 
    
    # Check for errors
    if len(possibleMatches) > 2:
        print possibleMatches
        raise AppError('''Could not identify sernum/modnum, \
        too many alphanumeric words''')
    elif len(possibleMatches) < 2:
        raise AppError('''To few matches found''')
    # Find which is longest
    matchLengths = [len(i) for i in possibleMatches]
    
    # Check lengths aren't identical
    if matchLengths[0]==matchLengths[1]:
        raise AppError('''Could not distinguish sernum as same 
        length as model num''')
    
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
        raise AppError('Too many names')
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
            temp.append(fuzz.partial_ratio(word, region))
        if max(temp) < 90:
            newList.append(word)
    return newList
        

                
    '''
    This version won't work as places can have longer names
def findRegion(words):
    possibleRegions = [] # Selected region
    matchWords = [] # Word which was matched
    matchAmount = [] # How closely words match
    for word in words:
        match = process.extract(word,regions,limit=1)
        if match[1] > 80:
            matchWords.append(word)
            possibleRegions.append(match[0])
            matchAmount.append(match[1])
    # Check for errors
    if len(possibleRegions) == 0:
        raise AppError('Could not identify a region')
    
    # Pick most likely match
    idx = matchAmount.index(max(matchAmount))
    words.remove(matchWords[idx])
    return possibleRegions[idx]
    '''