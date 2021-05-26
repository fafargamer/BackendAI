
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from nltk.stem.porter import PorterStemmer
from joblib import dump, load
import spacy
import io
from sklearn.feature_extraction import text
import numpy as np
from scipy.sparse.csr import csr_matrix
from nltk import ngrams
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity

def VectorizingSubstring(inputAA, inputPure, similarity): 

  moff = {"Pair":[],"Substring":[],"Similarity":[]}
  for i in range(len(inputAA)):
    for j in range(len(inputAA)):
      primoVictoria=[]
      numberSimilarity=0
      for iInd in range(len(inputAA[i])):
        stringSimilar=[]
        pointSimilarity = 0
        if(j < len(inputAA)):
          for jInd in range(len(inputAA[j])):
            if i!=j and j>i:
              similarityArray = []

              if len(inputAA[i]) == 1:
                similarityArray.append(inputAA[i][0])
              else:
                similarityArray.append(inputAA[i][iInd])

              if len(inputAA[j]) == 1:
                similarityArray.append(inputAA[j][0])
              else:
                similarityArray.append(inputAA[j][jInd])


              vectorizer = TfidfVectorizer(input=similarityArray, analyzer='word', ngram_range=(1,8),
                                          min_df = 0, stop_words='english')
              tfidf_matrix =  vectorizer.fit_transform(similarityArray)
              cosJ = cosine_similarity(tfidf_matrix)
              prevJI = []
              x=0
              for iVec in range(len(cosJ)):
                for jVec in range(len(cosJ[iVec])):
                  if i!=j and cosJ[iVec][jVec] > similarity and iVec!=jVec and ([iVec,jVec] not in prevJI) and ([jVec,iVec] not in prevJI):
                    prevJI.append([iVec,jVec])
                    if len(inputAA[i]) == 1:
                      aString = inputPure[i][0]
                    else:
                      aString = inputPure[i][iInd]

                    if len(inputAA[j]) == 1:
                      bString = inputPure[j][0]
                    else:
                      bString = inputPure[j][jInd]
                    stringSimilar.append([aString,bString])
                    pointSimilarity= pointSimilarity + cosJ[iVec][jVec]

        if(len(stringSimilar)>0):
          numberSimilarity = numberSimilarity + (pointSimilarity/len(inputAA[j]))
          primoVictoria.append(stringSimilar)

      if(len(stringSimilar)>0):
        totalSimilarity = numberSimilarity
        moff["Pair"].append([i,j])
        moff["Substring"].append(primoVictoria)
        moff["Similarity"].append(totalSimilarity)

  return moff