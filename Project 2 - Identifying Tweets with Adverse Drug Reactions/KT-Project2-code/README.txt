The package contains 4 folders and 12 files.

 

 - README.txt: this file describes the programs, data representation and predicted labels.

 


 ===  1. sentiment attribute programs ===

 

 - This file contains 3 programs, which separately generate sentiment attribute values for the train.txt, dev.txt and test.txt.



 - The sentiment analysis imported the vaderSentiment package 
   from https://pypi.python.org/pypi/vaderSentiment.

 
 
 - A compound sentiment score will be generated for each tweet. Tweets with positive scores will be identified as having positive sentiment and the attribute value will be 1. Otherwise, tweets will be assigned 0 for the sentiment attributes.





 === 2. side-effect attribute programs ===

  

 - This file contains 3 programs, which separately identify whether a tweet contains the bigram-word, “side effect” for the train.txt, dev.txt and test.txt.

  

 - The attribute value for tweets which have the bigram-word, “side effect”, will be 1. Otherwise, the side-effect attribute value will be 0.

 
 

 
 === 3. data representation (with new attributes) ===

  

 - This file contains 3 .arff files, which are the representation of the raw tweets and are suitable for use with Weka.

 
 
 - The .arff file has 83 attributes and 2 new attributes, the sentiment attribute and side-effect attribute.


 
 - “id”, “am”, “banana”,”can”,”i”,”is“,”it”,”pic”,”rt”,”was” have already been removed in the three files.

 


 === 4. predicted labels ===

  

 - This file contains predicted labels for the test data set.

  
 
 - Two machine learning methods are applied, the Naive Bayes and SVM. The results for both methods are generated and presented in this file.

 


  ===         End         ===
