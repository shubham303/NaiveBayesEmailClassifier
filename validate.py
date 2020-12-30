from pathlib import Path
import re
import json
from math import log
from math import exp
from classifer import isSpam
from Preprocess import  preProcessFiles


basepath = Path('dataset/test/ham')
preProcessFiles(basepath)

basepath = Path('dataset/test/spam')
preProcessFiles(basepath)




# program computer the accuracy of model on set of test emails
# 300 test spam emails
# 300 test ham emails
def classifyemails(test_email_list,spam_weights,ham_weights, spam_email_probablity, ham_email_probablity):
    spam_count=0
    ham_count=0
    for email in test_email_list:
        if(isSpam(email,spam_weights,ham_weights, spam_email_probablity, ham_email_probablity)):
            spam_count+=1
        else:
            ham_count+=1
    return(spam_count, ham_count)


basepath = Path('dataset/test/spam')
files_in_basepath = basepath.iterdir()

spam_emails = []
for file in files_in_basepath:
    spam_emails.append(file.read_text())

basepath = Path('dataset/test/ham')
files_in_basepath = basepath.iterdir()

ham_emails = []
for file in files_in_basepath:
    ham_emails.append(file.read_text())

weights = []
with open('weights.txt') as f:
    weights = list(f)

ham_email_probablity = float(weights[0])
spam_email_probablity = float(weights[1])
ham_weights = json.loads(weights[2])
spam_weights = json.loads(weights[3])


predicted_spam_emails, predicted_ham_emails=classifyemails(spam_emails,spam_weights,ham_weights, spam_email_probablity, ham_email_probablity)

print("total spam emails={}".format(len(spam_emails)))
print(predicted_spam_emails)
print(predicted_ham_emails)
print("accuracy={}%".format(100*predicted_spam_emails/len(spam_emails)))


predicted_spam_emails, predicted_ham_emails=classifyemails(ham_emails,spam_weights,ham_weights, spam_email_probablity, ham_email_probablity)

print("total ham emails={}".format(len(ham_emails)))
print(predicted_spam_emails)
print(predicted_ham_emails)
print("accuracy={}%".format(100*predicted_ham_emails/len(ham_emails)))

