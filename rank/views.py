# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import numpy as np
import pandas as pd

import nltk
import gensim
import operator
import sys
import time

class Model(object):
    def __init__(self, presaved_vectors_location, word2vec_model):
        self.model_link = word2vec_model
        self.saved_vectors = np.load(presaved_vectors_location)

    def get(self, word):
        if word in self.saved_vectors:
            return self.saved_vectors[word]


    def cosine_simiarity(self, vec_a, vec_b):
        return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))


word2vec_filename = 'rank/GoogleNews-vectors-negative300.bin.gz'

import pandas as pd
import nltk
import gensim
import operator
import sys
import time
import argparse

# Download necessary packages to use NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#Finds Nouns in a phrase/sentence excluding certain words
def getNouns(sentence, exclude_words):
    nouns = []
    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS') and word not in exclude_words:
            nouns.append(word)
    return nouns

#Find a similarity ranking based on the words by computing the average similarity
# score for a word in a category
def get_avg_similarity(query, list_of_words):
    total_score = 0
    if len(list_of_words) != 0:
        for word in list_of_words:
            try:
                score = model.similarity(word, query)
                total_score += score
            except KeyError:
                pass
                #Ignores the words that it can't find in the model
                #print "Not Found", word
        return round(total_score/len(list_of_words), 4)
    else:
        return 0

# Returns the maximum score
def get_max_similarity(query, list_of_words):
    max_score = 0
    for word in list_of_words:
        try:
            score = model.similarity(word, query)
            if score > max_score:
                max_score = score
        except KeyError:
            pass
            #Ignores the words that it can't find in the model
            #print "Not Found", word
    return round(max_score, 4)

# Returns the top 5 categories with highest scores
def highest_k_values(dictionary, num_results):
    return sorted(dictionary.iteritems(), key=operator.itemgetter(1), reverse=True)[:num_results]


start = time.clock()

model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_filename, binary = True)
# model = gensim.models.Word2Vec.load(sys.argv[1])

print "Time taken to load the model: %f" % (time.clock() - start)


#model = Model('saved_vectors.npy', word2vec_filename)

def get_rank(request):

    exclude_nouns = ["services", "products"]

    structure_csv = pd.read_csv("rank/final_structure.csv")
    structure_csv["2017 NAPCS Code"] = structure_csv["2017 NAPCS Code"].astype('str')

    #Get NAPCS Categories which are at the bottom of the Structure Hierarchy
    structure_csv = structure_csv[structure_csv["2017 NAPCS Code"].str.len() == 11]

    data = [tuple(x) for x in structure_csv[["2017 NAPCS Code" ,"Title"]].values ]

    query = request.POST.get('query')

    print query


    score_dict_first_method = {}
    score_dict_second_method = {}


    query = query.replace(" ", "_")

    if query not in model.vocab:
        return render(request, 'rank/rank.html', {'error' : True})

    for section_id, section in data:
        nouns = getNouns(section, exclude_nouns)
        score_first_method = get_avg_similarity(query, nouns)
        score_second_method = get_max_similarity(query, nouns)

        score_dict_first_method[(section_id, section)] = score_first_method
        score_dict_second_method[(section_id, section)] = score_second_method


    first =  highest_k_values(score_dict_first_method, 5)
    second =  highest_k_values(score_dict_second_method, 5)

    print first
    print second

    return render(request, "rank/rank.html", { "ranks": [("Average Similarity for a Category", first), ("Maximum Similarity Score for a Category", second)]})
