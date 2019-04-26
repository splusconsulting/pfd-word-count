
import PyPDF2
import csv
import re
import requests
import numpy as np
from collections import Counter

pdfFileObject = open('C:/Users/Philip Sutera/Desktop/S+ Consulting/Policy/City Budgets/test/2005_Test_Budget.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
count = pdfReader.numPages

word_list = list()
cap_words = list ()
final_words = list ()

for i in range(count):
    page = pdfReader.getPage(i)
    text = page.extractText()
    words = re.findall(r'\w+', text)
    word_ignore = ['AND','THE','OF','IN','TO','A','FOR','TO','BY','IS','ARE','FROM','ON','AS','WITH','THIS','OR','BE','AT','WHICH','OTHER','THESE','THAT','MORE',
                    'WAS','HAS','ITS','THAN','AN','BEEN','DURING','HAVE','WERE','ALSO','NOT','ALL','WHEN','EACH','BOTH','INTO','THEIR','HOWEVER','ABOUT','BUT',
                    'THERE','THEN','BECAUSE','THEY','HOW','SO','A','B','C','D','E','F','G','H','I','J','K','J','M','N','O','P','Q','R','S','T','U','V','W','X','Y'
                    ,'Z','(',')']

    for word in words:
        cap_words.append (word.upper())
        c=Counter(word.strip() for word in cap_words)
        word_set=set(cap_words)
        word_list = list(word_set)

for x in word_list:
    if x in word_ignore:
        pass
    else:
        final_words.append (x + ','+ str(c[x]))
        outputFile = open('2005.csv', 'wb')
        outputWriter = csv.writer(outputFile,delimiter=' ')
        for w in final_words:
            outputWriter.writerow([w])






#print word_list
#c=Counter(word.strip() for w in word_list)
#for x in c:
#    word_list.append (x + ','+ str(c[x]))
#    outputFile = open('page2.csv', 'wb')
#    outputWriter = csv.writer(outputFile,delimiter=' ')
#    for w in word_list:
#        outputWriter.writerow([w])

#for w in word_list:
#    c=Counter(word.strip() for w in word_list)
#    final_words.append (word + ','+ str(c[word]))
#    print final_words



#print word_set

#    c=Counter(word.strip() for word in cap_words)
#    for word in cap_words:
#        word_list.append (word + ','+ str(c[word]))
#    print word_list
