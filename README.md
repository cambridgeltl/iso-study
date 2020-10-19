# "Are All Good Word Vector Spaces Isomorphic": Data and Code 
Contact: [Ivan Vulić](https://sites.google.com/site/ivanvulic/) (iv250 AT cam DOT ac DOT uk)

This repo contains 1) bilingual lexicons, 2) sampled processed Wikipedia snapshots, and 3) code used in the empirical study [Are All Good Word Vector Spaces Isomorphic?](https://arxiv.org/pdf/2004.04070.pdf) (Vulić, Ruder, Søgaard EMNLP 2020)

### References

If you use any of the provided material in your own work, please cite the following paper:
```
@inproceedings{Vulic:2020iso,
  author    = {Vuli\'{c}, Ivan and Ruder, Sebastian and S{\o}gaard, Anders},
  title     = {Are All Good Word Vector Spaces Isomorphic?},
  booktitle = {Proceedings of the 2019 Conference 
              on Empirical Methods in Natural Language Processing (EMNLP)},
  year      = {2020},
  }
```

### Bilingual Lexicons
You can download all bilingual lexicons used in the paper [here](https://github.com/cambridgeltl/iso-study/raw/master/lexicons/BilingualLexicons.zip).

* The languages included are: English (en), Spanish (es), Arabic (ar), Japanese (ja), Quechuan (qu), Galician (gl), Basque (eu), Bengali (bn), Urdu (ur), Tamil (ta).

* The format of the lexicons should be self-explanatory. The files are tab-delimited.

* The provided lexicons are of course not perfect, and some of them have not been manually cleaned or verified although the extraction process from PanLex was quite strict in order to focus on high precision. Still, there might be some noise in the lexicons. Therefore, the lexicons should be considered as silver standard.

* For some language pairs (due to the strict extraction process), the number of pairs in the lexicons is smaller than the desired 5K training pairs or 2K test pairs - please double-check before running any size-related analyses of the lexicons and projection-based methods.

* Other details, such as the source of the lexicon (e.g., Google Translate, PanLex, manual translation) are available in the corresponding paper.


### Sampled Wikipedia Snapshots 
In the paper, we sample the Wikipedias of high-resource languages (e.g., Spanish) so that its topical distribution is as close as possible to that of low-resource languages spoken in similar regions (e.g., Galician, Basque) or related to it via historical links (e.g., Quechuan) - see subsection 4.6 in the paper.

We provide these sampled (and processed) Wikipedias: they can be obtained [here](link).


### Code: Isomorphism Scripts
We also provide Python (python2) scripts used to compute isomorphism scores with the three isomorphism measures used in the paper.


### Contact
* For any further questions, please contact [Ivan Vulić](https://sites.google.com/site/ivanvulic/) (iv250 AT cam DOT ac DOT uk)
