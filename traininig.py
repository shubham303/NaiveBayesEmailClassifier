from pathlib import Path
import re
import json
from math import log
from Preprocess import preProcessFiles


# Preprocess the data
basepath = Path('dataset/ham')
preProcessFiles(basepath)

basepath = Path('dataset/spam')
preProcessFiles(basepath)

# train the model using dataset and save parameters in weights.txt
print("training start")
basepath = Path('dataset/spam')
files_in_basepath = basepath.iterdir()

spam_emails = []   # list of spam emails
for file in files_in_basepath:
    spam_emails.append(file.read_text())

basepath = Path('dataset/ham')
files_in_basepath = basepath.iterdir()

ham_emails = []  # list of ham emails
for file in files_in_basepath:
    ham_emails.append(file.read_text())

spam_emails_count = len(spam_emails)
ham_emails_count = len(ham_emails)
total_emails = spam_emails_count+ham_emails_count

probablity_of_spam = spam_emails_count/total_emails
probablity_of_ham = ham_emails_count/total_emails

word_spam_probablity = {}
word_ham_probablity = {}

for text in spam_emails:
    words = text.split()
    words= list(dict.fromkeys(words))
    for word in words:
        word_spam_probablity[word] = word_spam_probablity.get(word, 0)+1
           
for text in ham_emails:
    words = text.split()
    words= list(dict.fromkeys(words))
    for word in words:
        word_ham_probablity[word] = word_ham_probablity.get(word, 0)+1


for k , v in word_ham_probablity.items():
    v=v/ham_emails_count
    s=log(v)
    t=log(1-v)
    word_ham_probablity[k]=(s,t)
for k , v in word_spam_probablity.items():
    v=v/spam_emails_count
    s=log(v)
    t=log(1-v)
    word_spam_probablity[k]=(s,t)


for k , v in word_ham_probablity.items():
    if(k not in word_spam_probablity):
        word_spam_probablity[k]=(log(0.0000615574),log(1-0.0000615574))

for k , v in word_spam_probablity.items():
    if(k not in word_ham_probablity):
        word_ham_probablity[k]=(log(0.0000615574),log(1-0.0000615574))


#save parameters

weights=open("weights.txt","w")

weights.write(str(log(probablity_of_ham))+'\n')
weights.write(str(log(probablity_of_spam))+'\n')

json.dump(word_ham_probablity, weights)
weights.write("\n")
json.dump(word_spam_probablity, weights)


print("training complete")