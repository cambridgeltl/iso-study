# -*- coding: utf-8 -*-
import numpy as np
import torch, gudhi
import sys, time, codecs
#import matplotlib.pyplot as plt

from sklearn.preprocessing import normalize
from scipy.spatial.distance import cosine

reload(sys)
sys.setdefaultencoding('utf8')

FREQ = 5000
HOMO_DIM = 1

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
    return words, input_dic

def distance_matrix(xx_freq, xx_vec):
    """
    This function computes distance matrices from the embedding matrices
    """
    xx_vectors = []
    for word in xx_freq[:FREQ]:
        xx_vectors.append(xx_vec[word])
    xx_embed_temp = np.vstack(xx_vectors)
    xx_embed = torch.from_numpy(xx_embed_temp)
    xx_dist = torch.sqrt(2 - 2 * torch.clamp(torch.mm(xx_embed, torch.t(xx_embed)), -1., 1.))
    xx_matrix = xx_dist.cpu().numpy()
    return xx_matrix

def compute_diagram(x, homo_dim=1):
    """
    This function computes the persistence diagram on the basis of the distance matrix
    and the homology dimension
    """
    rips_tree = gudhi.RipsComplex(x).create_simplex_tree(max_dimension=homo_dim)
    rips_diag = rips_tree.persistence()
    return [rips_tree.persistence_intervals_in_dimension(w) for w in range(homo_dim)]

def compute_distance(x, y, homo_dim = 1):
    start_time = time.time()
    diag_x = compute_diagram(x, homo_dim=homo_dim)
    diag_y = compute_diagram(y, homo_dim=homo_dim)
    #print("Filteration graph: %.3f" % (time.time() - start_time))
    return min([gudhi.bottleneck_distance(x, y, e=0) for (x, y) in zip(diag_x, diag_y)])


def main():
    # Get vectors first and words sorted by frequency
    en_freq, en_vec = load_word_vectors(sys.argv[1])
    de_freq, de_vec = load_word_vectors(sys.argv[2])

    # Step 1. Compute distance matrices from the top FREQ words
    # a) Source and b) Target
    en_matrix = distance_matrix(en_freq, en_vec)
    de_matrix = distance_matrix(de_freq, de_vec)

    # Step 2. Get the actual distance based on matrices and the
    # persistance diagrams
    print "Gromov-Hausdorff: ", compute_distance(en_matrix, de_matrix)
        
# The code starts here
if __name__=='__main__':
    main()
