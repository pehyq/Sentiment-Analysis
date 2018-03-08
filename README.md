# Sentiment-Analysis
Sentiment analysis of microblog data 

### Objective
The sentiment of tweets is an important task that helps to determine the users’ perceptions of organizations, events or products. This assignment aims to develop a classifier to classify input stream of tweets into multiple sentiment classes (the simplest being just the positive, negative and neutral classes). One important resource in sentiment analysis is the dictionary of sentiment vocabulary, or sentiment lexicon, which may vary according to time (new sentiment terms may emerge) and classes or aspects (same term may have different sentiments with respect to different classes or aspects). Additionally, there are other data sources that will help enhance the project such as various social factors etc.

### Environment Setting
Python 3.6.3 |Anaconda custom (64-bit)| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)]

### Installation 
1. nltk 
2. simplejson
3. numpy
4. scipy
5. scikit-learn
6. emoji

If you use the VADER sentiment analysis tools, please cite:
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

### Usage 
1. Run 'Step1_preprocess_emoji.py' to prepocess tweet content, including data cleaning (e.g., remove url, punctuations, time), and handle emoji.
2. Run 'Step2_sentiment_analyzer_late_fusion.py' which performs the following:
- load preprocessed data
- perform handling of cases as per VADER
- perform valance scoring as per VADER
- include social features as enhancer
- outputs optimal precision, recall and f1 score of the default model, best model
