import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle



def nbclassfy(train_file='Webpages_Classification_test_data.csv', model='nb_model.sav'):
    train_news = pd.read_csv(train_file)
    tfidf = TfidfVectorizer(stop_words='english', use_idf=True, smooth_idf=True)  # TF-IDF

    svm_pipeline = Pipeline([('lrgTF_IDF', tfidf), ('lrg_mn', MultinomialNB())])

    filename = model
    pickle.dump(svm_pipeline.fit(train_news['content'].values.astype('U')[0:100000], train_news['label'][0:100000]), open(filename, 'wb'))

    print("Model Successfully Trained")


def main():
	nbclassfy('Webpages_Classification_test_data.csv','nb_model.sav')

if __name__ == '__main__':
	main()