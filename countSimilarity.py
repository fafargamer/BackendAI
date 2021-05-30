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

        stringSimilar=[]
        numberSimilarity=0

        for iInd in range(len(inputAA[i])):
          
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
              
                print(similarityArray)

                vectorizer = TfidfVectorizer(input=similarityArray, analyzer='word', ngram_range=(1,10),
                                            min_df = 0,smooth_idf=True,use_idf=True,stop_words='english')
                tfidf_matrix =  vectorizer.fit_transform(similarityArray)
                matrix = tfidf_matrix.toarray()

                similarityMatrix = cosine_similarity(matrix)
                totalSimilarityNow = similarityMatrix[0][1]
                print('Similarity part : {}'.format(totalSimilarityNow))



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

                  stringSimilar.append([aString,bString])

                pointSimilarity= pointSimilarity + totalSimilarityNow


          # Add similarity
          numberSimilarity = numberSimilarity + pointSimilarity
            
        

        # Count Total Similarity
        totalSimilarity = numberSimilarity/(max(len(inputAA[i]),len(inputAA[j])))

        print('Total similarity : {}'.format(totalSimilarity))

        # Append to Response
        if(totalSimilarity > similarity):
          moff["Pair"].append([i,j])
          moff["Substring"].append(stringSimilar)
          moff["Similarity"].append(totalSimilarity)

  return moff