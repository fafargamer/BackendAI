import urllib
import spacy
import requests
import string
import docx
import io
import re
import numpy as np
from nltk.tokenize import RegexpTokenizer
from string import digits
from docx import Document   #pip install python-docx
import PyPDF2               #pip install PyPDF2

# import StopWordRemoverFactory class
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary #pip install Sastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from stopwords import more_stopword as more_St

factory = StopWordRemoverFactory()
# factoryStem = StemmerFactory()
# stopword = factory.create_stop_word_remover()
# stemmer = factoryStem.create_stemmer()
import re # impor modul regular expression

# Ambil Stopword bawaan
stop_factory = StopWordRemoverFactory().get_stop_words()

# Merge stopword
data = stop_factory + more_St
 
dictionary = ArrayDictionary(data)
stopword = StopWordRemover(dictionary)

def PPDFP(document):

  #Download and Save
  # document = requests.get(inputURL, allow_redirects=True)
  open('testPDF.pdf', 'wb').write(document.content)

  #Open PDF
  pdfFileObj = open('testPDF.pdf', 'rb')
  pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

  #Extract Text
  global pdfTexts
  pdfTexts=[]
  returnText=[]
  pureText=[]
  for i in range(pdfReader.numPages):
    page = pdfReader.getPage(i)
    pageText = page.extractText()
    pageText = pageText.replace('\n \n', ']]n]]nn]]n]]n]n')
    pageText = pageText.split("]]n]]nn]]n]]n]n")
    for i in range(len(pageText)):
        newText = pageText[i].replace('\n', '"')
        newText = newText.replace('\"', '')
        newText = newText.replace('\u00a0', '')
        if(len(newText)>0 and newText != " "):
          returnText.append(newText)
          pureText.append(newText)
          

  result = []
  s=""
  for i in range(len(returnText)):
      text = []
      for j in range(len(returnText[i])):
        
        tokenizer = RegexpTokenizer(r'\w+')
        textsTokenized=tokenizer.tokenize(returnText[i][j])
        if(len(textsTokenized) < 1):
          textsTokenized = [' ']
        # if textTokenized == ['\u00a0']:
        #   textsTokenized = ['']
        text.append(textsTokenized[0])

      textor = s.join(text)
      textor = stopword.remove(textor)
      # textor = stemmer.stem(textor)
      textor = re.sub(r"\d+", "", textor)
      result.append(textor)


  dividedDocument = []
  dividedPure = []

  # print(result)
  print('Document Processed')

  divisor = 1

  if len(result) > 255:
    # print(len(result))
    # print('Dokumen dapat dibagi 5')

      document_split = np.array_split(result, int(len(result)/(divisor*64)))
      pure_split = np.array_split(pureText, int(len(pureText)/(divisor*64)))

      for i in range(len(document_split)):
        # print("Part : {}".format(pure_split[i]))
        joinedDocument = ' '.join(document_split[i])
        joinedPure = ' '.join(pure_split[i])
        dividedDocument.append(joinedDocument)
        dividedPure.append(joinedPure)

      result = dividedDocument
      pureText = dividedPure


  elif len(result) > 127:
    # print(len(result))
    # print('Dokumen dapat dibagi 5')

      document_split = np.array_split(result, int(len(result)/(divisor*32)))
      pure_split = np.array_split(pureText, int(len(pureText)/(divisor*32)))

      for i in range(len(document_split)):
        # print("Part : {}".format(pure_split[i]))
        joinedDocument = ' '.join(document_split[i])
        joinedPure = ' '.join(pure_split[i])
        dividedDocument.append(joinedDocument)
        dividedPure.append(joinedPure)

      result = dividedDocument
      pureText = dividedPure


  elif len(result) > 63:
    # print(len(result))
    # print('Dokumen dapat dibagi 5')

      document_split = np.array_split(result, int(len(result)/(divisor*16)))
      pure_split = np.array_split(pureText, int(len(pureText)/(divisor*16)))

      for i in range(len(document_split)):
        # print("Part : {}".format(pure_split[i]))
        joinedDocument = ' '.join(document_split[i])
        joinedPure = ' '.join(pure_split[i])
        dividedDocument.append(joinedDocument)
        dividedPure.append(joinedPure)

      result = dividedDocument
      pureText = dividedPure


  elif len(result) > 31:
    # print(len(result))
    # print('Dokumen dapat dibagi 5')

      document_split = np.array_split(result, int(len(result)/(divisor*8)))
      pure_split = np.array_split(pureText, int(len(pureText)/(divisor*8)))

      for i in range(len(document_split)):
        # print("Part : {}".format(pure_split[i]))
        joinedDocument = ' '.join(document_split[i])
        joinedPure = ' '.join(pure_split[i])
        dividedDocument.append(joinedDocument)
        dividedPure.append(joinedPure)

      result = dividedDocument
      pureText = dividedPure


  elif len(result) > 15:
    # print(len(result))
    # print('Dokumen dapat dibagi 5')

      document_split = np.array_split(result, int(len(result)/(divisor*4)))
      pure_split = np.array_split(pureText, int(len(pureText)/(divisor*4)))

      for i in range(len(document_split)):
        # print("Part : {}".format(pure_split[i]))
        joinedDocument = ' '.join(document_split[i])
        joinedPure = ' '.join(pure_split[i])
        dividedDocument.append(joinedDocument)
        dividedPure.append(joinedPure)

      result = dividedDocument
      pureText = dividedPure

  elif len(result) > 7:
    # print(len(result))
    # print('Dokumen dapat dibagi 5')
      document_split = np.array_split(result, int(len(result)/(divisor*2)))
      pure_split = np.array_split(pureText, int(len(pureText)/(divisor*2)))

      for i in range(len(document_split)):
        # print("Part : {}".format(pure_split[i]))
        joinedDocument = ' '.join(document_split[i])
        joinedPure = ' '.join(pure_split[i])
        dividedDocument.append(joinedDocument)
        dividedPure.append(joinedPure)

      result = dividedDocument
      pureText = dividedPure


  print('Length : {}'.format(len(pureText)))

  return pureText, result