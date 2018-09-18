Student Number: 843282       Student Name: Yue Cao

The package contains 3 folders and 16 files:

- README.txt: this file describes Programs, Dataset and Program Results.

  ==== 1. DATA & DICT ====

  - dict.txt: is vocabulary contains 234371 words will be used as a source for approximate matching. 

  - labelled-tokens.txt: is a list of tokens drawn from "Tweets". These tokens are our candidates for analysing lexical normalisation of Twitter data. Each token is formated as "Token TAB Code TAB Canonical_Form".
    
  - Slang_dict.txt: a slang dictionary (Slang-dict.txt) curated by Fei Liu et al (2012),which comprises 3802 non-standard tokens along with their canonical forms.
     
    Data Set Reference: Liu, F., Weng, F., & Jiang, X. (2012, July). A broad-coverage normalization system for social media language. In Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics: Long Papers-Volume 1 (pp. 1035-1044). Association for Computational Linguistics. Accessed from http://www.hlt.utdallas.edu/~yangl/data/Text_Norm_Data_Release_Fei_Liu/)


  ==== 2. PROGRAMS ====
  
  - All the programs are written in python 3.6.2.
  
  - Only "OOV" tokens will be normalised. 

  - 0-OOV-analysis.py: is a program which analysis the proportion of "OOV" tokens which have canonical forms the same as themselves.It is indicated that these tokens should not be normalised.

  - 1-editdistance-single prediction.py: is a program which implements Global Edit Distance and returns a single prediction as "Best match" for each token along with Token, Canonical Form, and best Levenshtein Distance. The single prediction is the first word in vocabulary which has the minimum Global Edit Distance. In addition, this program also calculate the accuracy of the system.
    The "editdistance" package is imported from "https://pypi.python.org/pypi/editdistance" (Tanaka 2016).

  - 2-editdistance-multiple prediction.py: is similar to "1-editdistance-multiple prediction" except that this program returns multiple predictions which have the minimum Global Edit Distance. The precision and recall of the system are calculated.

  - 3-GED+N-Gram.py: combines Global Edit Distance method with N-Gram Distance to increase the system precision. In this program, multiple predictions for each token will be stored in a best_matches_list. Then match(es) has the best score in 2-Gram Distance will be returned.
    The "Ngram" package is imported from "https://pypi.python.org/pypi/ngram"(Poulter 2017).
    
  - 4-GED+refined soundex.py: combines Global Edit Distance method with Refined Soundex Method to conduct approximate mathching. Refined Soundex method will be used to identify the best match from multiple predictions returned by Global Edit Distance Method. The precision and recall of system are also calculated in the system
    The ¡°pyphonetics¡± package is imported from "https://pypi.python.org/pypi/pyphonetics/0.4.1"(Lilykos 2016).
    It is noted that digits are not included in the analysis of this system.

  - 5-Slang+GED+RefinedSoundex.py: Firstly, this system applies a slang dictionary(Slang_dict.txt) curated by Fei Liu (2012) as a white list for non-standard tokens which are frequently used slangs. Then repeat the approaches the same as program 4, the GED and Refined Soundex.
    It is noted that digits are not included in the analysis of this system.


  ==== 3. RESULTS ====
  
   In this folder, results for the six programs above are presented. 

  ====       End      ====



