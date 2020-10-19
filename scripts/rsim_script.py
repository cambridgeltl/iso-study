# -*- coding: utf-8 -*-
#import matplotlib.pyplot as plt
#import networkx.algorithms.isomorphism as iso
import sys,codecs
from scipy.spatial.distance import cosine
from scipy.stats import pearsonr
import numpy as np

from sklearn.preprocessing import normalize

import operator, time
reload(sys)
sys.setdefaultencoding('utf8')

PAIRS = 1000

def normalise_word_vectors(word_vectors, norm=1.0):
    """
    This method normalises the collection of word vectors provided in the
    word_vectors dictionary.
    """
    for word in word_vectors:
        word_vectors[word] /= math.sqrt((word_vectors[word]**2).sum() + 1e-6)
        word_vectors[word] = word_vectors[word] * norm
    return word_vectors


def load_word_vectors(file_destination):
    """
    This method loads the word vectors from the supplied file destination.
    It loads the dictionary of word vectors and prints its size and the vector
    dimensionality.
    """
    print >> sys.stderr, "Loading vectors from", file_destination
    input_dic = {}

    with open(file_destination, "r") as in_file:
        lines = in_file.readlines()

    in_file.close()

    words = []
    vectors = []
    for line in lines[1:]:
        item = line.strip().split()
        dkey = item.pop(0)
	words.append(dkey)
        vector = np.array(item, dtype='float32')
        vectors.append(vector)
	#print np.mean(vector)

    npvectors = np.vstack(vectors)
    
    # Our words are stored in the list words and...
    # ...our vectors are stored in the 2D array npvectors

    # 1. Length normalize
    npvectors = normalize(npvectors, axis=1, norm='l2')

    # 2. Mean centering dimesionwise
    npvectors = npvectors - npvectors.mean(0)

    # 3. Length normalize again
    npvectors = normalize(npvectors, axis=1, norm='l2')

    # Create the final dictionary    
    for i in xrange(len(words)):
        word = words[i]
        vector = npvectors[i]
        input_dic[word] = vector
    
    print >> sys.stderr, len(input_dic), "vectors loaded from", file_destination
    return input_dic

def main():
    en_dict=[l.strip().split()[0] for l in open(sys.argv[3]).readlines()][:PAIRS]
    de_dict=[l.strip().split()[1] for l in open(sys.argv[3]).readlines()][:PAIRS]

    en_vec = load_word_vectors(sys.argv[1])  
    de_vec = load_word_vectors(sys.argv[2]) 
    en_dists=[]
    de_dists=[]

    # First check - check that all the words do have actual vectors
    #print en_dict
    #print de_dict

    for w in en_dict:
	if w not in en_vec:
	    print >> sys.stderr, "Problem with...", w
            rvector = np.random.rand(300,1).flatten()
            rvector = np.array(rvector, dtype='float32')
            rvector = rvector/np.linalg.norm(rvector)
            en_vec[w] = rvector

    
    for w in de_dict:
        if w not in de_vec:
            print >> sys.stderr, "Problem with...", w
            rvector = np.random.rand(300,1).flatten()
            rvector = np.array(rvector, dtype='float32')
            rvector = rvector/np.linalg.norm(rvector)
            de_vec[w] = rvector

    # Get source language second-order distances
    for w in en_dict:
        for v in en_dict:
            if w!=v: 
                en_dists.append(np.dot(en_vec[w],en_vec[v]))

    # Get target lanuage second-order distances
    for w in de_dict:
        for v in de_dict:
            if w!=v: 
                de_dists.append(np.dot(de_vec[w],de_vec[v]))
    
    print >> sys.stdout, "Pearson:", pearsonr(en_dists,de_dists)
  
# The code starts here
if __name__=='__main__':
    main()
