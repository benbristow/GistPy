#!/usr/bin/env python
#Designed for Python 2
#By Ben Bristow - http://github.com/benbristow/

import sys
import os.path
import simplejson as json
import requests
import pyperclip #Requires xclip on Linux

def checkFileExists(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False

def gistUpload(filename):
    #Read file into string
    data = ""
    with open(filename, "r") as inputFile:
        data = inputFile.read()
    
    #Encode JSON
    jsonoutput = json.dumps(
        {
            "description": "Uploaded with GistPy",
            "public": True,
            "files": {
                "file1.txt": {
                    "content": data
                }
            }
        }
    )
    
    #POST to Github and get response
    post_data = jsonoutput
    post_response = requests.post(url='https://api.github.com/gists', data=post_data)
    responsejson = post_response.text
    
    #Parse JSON
    j = json.loads(responsejson)
    url = j['html_url']
    pyperclip.copy(url)
    print "Successful! Link copied to clipboard."
    print url
    
#Main program

#Check if no arguments
if len(sys.argv) == 1:
    print "No input file specified."
else:
    filenames = sys.argv
    del filenames[0]
    for filename in filenames:
        if checkFileExists(filename):
            gistUpload(filename)
        else:
            print filename + " does not exist"
