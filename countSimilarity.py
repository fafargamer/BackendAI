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

      if i!=j  and j>i:
        primoVictoria=[]
        stringSimilar=[]
        numberSimilarity=0

        for iInd in range(len(inputAA[i])):
          
          pointSimilarity = 0

          if(j < len(inputAA)):

            for jInd in range(len(inputAA[j])):
              if i!=j and j>i:
                similarityArray = []
                # print('Dokumen ke-{} dan {}'.format(i,j)) 

                if len(inputAA[i]) == 1:
                  similarityArray.append(inputAA[i][0])
                else:
                  similarityArray.append(inputAA[i][iInd])

                if len(inputAA[j]) == 1:
                  similarityArray.append(inputAA[j][0])
                else:
                  similarityArray.append(inputAA[j][jInd])
              
                print(similarityArray)

                vectorizer = TfidfVectorizer(input=similarityArray, analyzer='word', ngram_range=(3,6),
                                            min_df = 0,smooth_idf=True,use_idf=True,stop_words='english')
                tfidf_matrix =  vectorizer.fit_transform(similarityArray)
                matrix = tfidf_matrix.toarray()

                similarityMatrix = cosine_similarity(matrix)
                totalSimilarityNow = similarityMatrix[0][1]
                print('Similarity part : {}'.format(totalSimilarityNow))
                # print(similarityArray[0])
                # print(similarityArray[1])
                # print(totalSimilarityNow)

                # cosJ = cosine_similarity(tfidf_matrix[0][1])
                # prevJI = []
                # x=0
                # for iVec in range(len(cosJ)):
                  # for jVec in range(len(cosJ[iVec])):
                    # if i!=j and iVec!=jVec and ([iVec,jVec] not in prevJI) and ([jVec,iVec] not in prevJI):
                if totalSimilarityNow > 0.1:
                  # prevJI.append([iVec,jVec])
                  if len(inputAA[i]) == 1:
                    aString = inputPure[i][0]
                  else:
                    aString = inputPure[i][iInd]

                  if len(inputAA[j]) == 1:
                    bString = inputPure[j][0]
                  else:
                    bString = inputPure[j][jInd]
                        # stringSimilar.append(aString)
                        # stringSimilar.append(bString)
                  stringSimilar.append([aString,bString])
                # print(cosJ[iVec][jVec])
                pointSimilarity= pointSimilarity + totalSimilarityNow
                      # print("{} - {} - {}".format(iInd,jInd,cosJ[iVec][jVec])
          # print(pointSimilarity)
          # if(len(stringSimilar)>0):
          numberSimilarity = numberSimilarity + pointSimilarity
            
        # primoVictoria.append(stringSimilar)

        # print(numberSimilarity)
        totalSimilarity = numberSimilarity/(max(len(inputAA[i]),len(inputAA[j])))
        # print("Total Parts : ".format(len(inputAA[i])*len(inputAA[j])))
        print('Total similarity : {}'.format(totalSimilarity))
        # print(totalSimilarity)
        if(totalSimilarity > similarity):
          moff["Pair"].append([i,j])
          moff["Substring"].append(stringSimilar)
          moff["Similarity"].append(totalSimilarity)

  return moff