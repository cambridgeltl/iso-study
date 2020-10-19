The simple python scripts can be called by specifying two (GH and EVS) or three arguments (RSIM) from the command line. The arguments specify the paths to source-language and target-language word embeddings (provided in the standard word2vec text format).

The third argument in the RSIM script specifies the path to the word translation dictionary used to compute the scores (e.g., for EN-ES computations we rely on the HFREQ, MFREQ, and LFREQ dictionaries). 

Additional hyper-parameters such as the vocabulary cut-off and/or preprocessing regimes can be specified by manipulating the Python code directly.

The code also relies on some 3rd party Python libraries such as scikit-learn, gudhi, and networkx (along with scipy, numpy, etc.)
