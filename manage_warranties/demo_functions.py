import re
from text_funs import findRegion, removeRegions
from Warranty_bank.settings import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID # This is only used when you want to send a forwarding message onto my phone. 
import twilio.twiml

class DemoError(Exception):
    """ Class for all my errors from this app"""
    pass

# Function deals dictionary into reply string.
def generateSuccessReplyDemo(detailDict):
    msgText = (
        'Thankyou for registering. Your details are: \n'
        'Name - %(Name)s, \n'
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
    name = ' '.join(words)
    
    detailDict = {
    'Name' : name,
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

# Historical view used to perform the demonstration. No longer needed in this simple form.
def demoDayTextHandler(request):
    # Overarching try statement just in case
    errormessage = 'Sorry your information could not be read. ' \
                'Guess thats the way with live demos...'
    resp = twilio.twiml.Response()
    try:
        msgText = request.POST.__getitem__('Body')
        print msgText
    except Exception as e:
        print e
    # Try to get details
    try:
        details = getTextInfoSimple(msgText)
        resp.message(generateSuccessReplyDemo(details))
        # Send message to my phone - comment out to stop sending these
        '''client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        msg = client.messages.create(to="+447759339709",
                              from_="+441475866042",
                              body = generateSuccessReplyDemo(details))
        #print generateSuccessReplyDemo(details)'''
    except DemoError as e:
        print e
        resp.message(errormessage)
    except DemoError as e:
        print e
        resp.message(errormessage)
    except Exception as e:
        print e
        resp.message(errormessage)

    return resp


