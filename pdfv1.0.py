
import PyPDF2
import csv
import re
import requests
import numpy as np
from collections import Counter

pdfFileObject = open('C:/Users/Philip Sutera/Desktop/S+ Consulting/Policy/City Budgets/test/2005AdoptedBudget.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
count = pdfReader.numPages

word_list = list()
cap_words = list ()

for i in range(count):
    page = pdfReader.getPage(i)
    text = page.extractText()

    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    words = re.findall(r'\w+', text)

    word_ignore = ['IF','THE','COOKIE','COOKIES','2015','A','AND','TO','2016','OF','WITH','FOR','ON','IN','THAT','AT','WE','OUR','CAREERS','NEW','US','COMPANY',
        'FEATURED','YOUR','SEARCH','LATEST','YOU','WHAT','ARTICLE','READ','APRIL','TRY','WELCOME','THEY','TED','PLAY','WAY','VIDEO','WORK','JANUARY','ARE','CAN','NOW','START','NEXT','ONLY','COMMENT','COMMENTS',
        'NAME','CANADA','MONTHS','FINDER','TEL','FROM','INC','EMEA','HIGH','APR','OCT','DEC','NOV','MAY','SEP','USA','CHINA','MEXICO','FRANCE','SITE',
        '']

    for word in words:
        cap_words.append (word.upper())

    c=Counter(word.strip() for word in cap_words)
    for x in c:
        if x in word_ignore:
            pass
        else:
            word_list.append (x + ','+ str(c[x]))
            outputFile = open('2005.csv', 'wb')
            outputWriter = csv.writer(outputFile,delimiter=' ')
            for wd in word_list:
                outputWriter.writerow([wd])
