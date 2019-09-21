import numpy as np
import random as random
import io


def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    for line in fin:
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = map(float, tokens[1:])
    return data


vector_data = load_vectors("wiki-new-300d-1M.vec")


def normalization (data):
    return [np.percentile(data, 10),
           np.percentile(data, 20),
           np.percentile(data, 30),
           np.percentile(data, 40),
           np.percentile(data, 50),
           np.percentile(data, 60),
           np.percentile(data, 70),
           np.percentile(data, 80),
           np.percentile(data, 90),
           np.percentile(data, 100)]


def assign_plus_minus_values_tuple (word):
    good_score = np.linalg.norm(np.array(vector_data[word]-vector_data["good"]))
    bad_score = np.linalg.norm(np.array(vector_data[word]-vector_data["bad"]))
    return good_score, bad_score


list_plus = []
list_minus = []
for word in vector_data:
    list_plus.append(assign_plus_minus_values_tuple(word)[0])
    list_minus.append(assign_plus_minus_values_tuple(word)[1])
normalized = normalization(list_plus), normalization(list_plus)


def do_stuff_comment (comment):
    scores = []
    for index in range(len(comment)-2):
        scores.append(assign_plus_minus_values_tuple(comment[index]),
                      assign_plus_minus_values_tuple(comment[index+1]),
                      assign_plus_minus_values_tuple(comment[index+2]))
    return scores

+

def



