from flask import Flask, request
from flask import jsonify
import urllib
import requests
import string
import io
import json
from json import dumps, loads, JSONEncoder, JSONDecoder
from flask import Response
# from processDocxOverallAllParagraph import processDocxParagraph
# from processPDFOverParagraph import PPDFP
# from vectorizerOveralloneAtATimeSubstring import VectorizingSubstring


app = Flask(__name__)



# urlDocx = "https://storage.googleapis.com/capstone-similarity-check/user_5f70438841f01404d05a291a_folder_5f89b71b563b456e643f357b_1603936983840.docx"

@app.route("/")
def hello():
    return "Hello!!!!"
    # return "Wot!"


# @app.route('/cek-kemiripan',  methods=["POST"])
# def process_paragraph_all():
#     data = request.get_json()

#     URLList = data['URLlist']
#     similarity = data['similarity']

#     pureDocumentArray = []
#     documentArray = []
#     for i in range(len(URLList)):
#         fileD = requests.get(URLList[i], allow_redirects=True)
#         print('Downloaded')
#         if (fileD.headers.get('content-type') == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"):
#             print("file is Docx")
#             a, b = processDocxParagraph(fileD)
#             pureDocumentArray.append(a)
#             documentArray.append(b)
#         elif (fileD.headers.get('content-type') == "application/pdf"):
#             print("file is PDF")
#             a, b = PPDFP(fileD)
#             pureDocumentArray.append(a)
#             documentArray.append(b)
#             # testDocXBatch.append(processPDFOverall(fileD))
#         else:
#             print("Does not support file type") 
        
#         # a, b = processDocxParagraph(fileD)


#     print(pureDocumentArray)
#     print(documentArray)

#     vector = VectorizingSubstring(documentArray, pureDocumentArray, similarity)
    

#     return json.dumps(vector)


if __name__ == "__main__":
    app.run()

# msg = "Hello world!"
# print(msg)

