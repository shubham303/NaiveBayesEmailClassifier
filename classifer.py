from pathlib import Path
import re
import json
from math import log
from math import exp

def isSpam(email,spam_weights,ham_weights, spam_email_probablity, ham_email_probablity):
    words = email.split()
    words=dict.fromkeys(words)
    spam_probablity = (spam_email_probablity)
    ham_probablity = (ham_email_probablity)
    
    
    for key, value in spam_weights.items():
       # print(exp(value[0]), " ", exp(value[1]), " " , exp(value[0])+exp(value[1]))
        if(key in words):
            spam_probablity += value[0]
        else:
            spam_probablity +=value[1]

    for key, value in ham_weights.items():
        if(key in words):
            ham_probablity += value[0]
        else:
            ham_probablity +=value[1]
            
    
    if(spam_probablity>ham_probablity):
        return True
    return False
