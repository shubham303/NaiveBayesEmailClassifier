from pathlib import Path
import re
import json
from math import log
from math import exp
from classifer import isSpam
from Preprocess import preProcessFiles

weights = []
with open('weights.txt') as f:
    weights = list(f)

ham_email_probablity = float(weights[0])
spam_email_probablity = float(weights[1])
ham_weights = json.loads(weights[2])
spam_weights = json.loads(weights[3])


basepath = Path('test')
preProcessFiles(basepath)

outputFile = open("output.txt", "w")
output = ""

files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    email = item.read_text()
    if(isSpam(email, spam_weights, ham_weights, spam_email_probablity, ham_email_probablity)):
        output += " 1"
    else:
        output += " 0"

outputFile.write(output)

print("output is written in output.txt")
