# Sentiment-Analysis
Sentiment analysis of microblog data 

### Objective
To develop a classifier to classify input stream of tweets into multiple sentiment classes (positive, negative and neutral classes). Other feaures such as emoji handling and social features were also added to improve classification accuracy.

The dataset is not uploaded due to privacy issues, it interested please contact me.

### Program structure
The programme consists of the following:
1.	Pre-processing of text data including emoji
2.	Handling of cases (VADER)
3.	Classification to get a Valance score (VADER)
4.	Enhancement with other features such as social features 
5.	Testing and optimisation based on precision, recall, and f1 scores

If you use the VADER sentiment analysis tools, please cite:
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

### Environment Setting
Python 3.6.3 |Anaconda custom (64-bit)| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)]

### Installation 
1. nltk 
2. simplejson
3. numpy
4. scipy
5. scikit-learn
6. emoji


### Usage 
1. Run 'Step1_preprocess_emoji.py' to prepocess tweet content, including data cleaning (e.g., remove url, punctuations, time), and handle emoji.
2. Run 'Step2_sentiment_analyzer_late_fusion.py' which performs the following:
- load preprocessed data
- perform handling of cases as per VADER
- perform valance scoring as per VADER
- include social features as enhancer
- outputs optimal precision, recall and f1 score of the default model, best model
