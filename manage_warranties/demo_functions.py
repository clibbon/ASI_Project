import re
from text_funs import findRegion, removeRegions, selectProperNouns, getNames

class DemoError(Exception):
    """ Class for all my errors from this app"""
    pass

# Function deals dictionary into reply string.
def generateSuccessReplyDemo(detailDict):
    msgText = (
        'Thankyou for registering. Your details are: \n'
        'Name - %(ForeName)s %(SurName)s, \n'
        'SerNo -  %(SerNo)s, \n' 
        'Region %(Region)s. \n'
        'Enjoy your ASI demo day!'
        % detailDict)
    return msgText

# Returns a simplified version of the text processing
def getTextInfoSimple(message, debug=False):
    # Remove all non alpha numeric characters
    message = re.sub(r'([^\s\w]|_)+', '', message) 
        
    # Split the text up
    words = message.split()
    # Identify model no and serial no
    serNum, words = findSerNum(words)
    if debug:
        print "After identification of serial/model num"
        print serNum, words
    # Find the region
    region = findRegion(message.lower())
    if debug:
        print "Region found is %s" % region
    # Remove any region matches
    words = removeRegions(words, region)
    # Remove non-Proper-nouns
    # Replaced - properNouns = selectProperNouns(words)
    
    
    # Find the names
    forename, surname = getNames(words)
    
    detailDict = {
    'ForeName' : forename,
    'SurName' : surname,
    'SerNo' : serNum,
    'Region': region
    }
    return detailDict

# Function finds the only alphanumeric word. Is a simplified version of findModelNums
# TODO: change to a function which just finds alphanums, and then add some logic
def findSerNum(words):
    possibleMatches = [] 
    for word in words:
        if not re.match("^[A-Za-z]+$", word): 
            possibleMatches.append(word) 
    
    # Check for errors
    if len(possibleMatches) > 1:
        print possibleMatches
        raise DemoError(
            'Could not identify serial number'
            ' too many alphanumeric words')
    elif len(possibleMatches) == 0:
        raise DemoError(
            'No possible matches found')
    
    serNum = possibleMatches[0]
    # Remove words from list
    words.remove(serNum)
    return (serNum, words)





