#!/usr/bin/env python3

import pickle
import argparse
import yaml
from collections import defaultdict
import numpy as np
from sortedcontainers import SortedDict

from get_keywords import get_keyword_extractor
from query import similarity_function

def compute_docwise_similarity(index, keywords):
    print('Message Keywords: %s' % keywords)

    scores = defaultdict(lambda: 0)
    nums = defaultdict(lambda: 0)
    similarity = similarity_function('exact')

    for keyword, _ in keywords:
        for indexed_keyword, indexed_entries in index.items():
            for score, doc in indexed_entries:
                curr_similarity = similarity(keyword, indexed_keyword)
                scores[doc] += np.exp(-score) * curr_similarity
                nums[doc] += 1

    # Normalize.
    for doc in scores:
        if scores[doc] != 0:
            scores[doc] /= nums[doc]

    return scores

def dot(d1, d2):
    sum = 0
    for key in d1:
        sum += d1[key] * d2[key]
    return sum

if __name__ == "__main__":

    # Parse command-line options.
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('message_file', default='sample_message.txt',
                        help='File containing message.')
    parser.add_argument('labels_file', default='labels.yaml',
                        help='YAML labels file.')
    parser.add_argument('index_file', default='index.pkl',
                        help='Index file.')

    args = vars(parser.parse_args())

    # Load everything.
    message_file = args['message_file']
    with open(args['labels_file'], 'r') as f:
        labels = yaml.safe_load(f)
    with open(args['index_file'], 'rb') as f:
        index = pickle.load(f)

    # Extract keywords.
    message_keywords = get_keyword_extractor('yake')(message_file, 20)
    
    # Compute similarities.
    similarities = compute_docwise_similarity(index, message_keywords)
    similarities_sorted = SortedDict({-score: doc for doc, score in similarities.items()})    

    # Predict label based on most similar documents.
    num_closest = min(len(similarities_sorted), 5)
    predicted_label = 0
    sum_scores = 0
    for neg_score, doc in similarities_sorted.items()[:num_closest]:
        predicted_label +=  -neg_score * labels[doc]
        sum_scores += -neg_score
    predicted_label /= sum_scores

    print('\nMost similar documents: %s' % {doc: -neg_score for neg_score, doc in similarities_sorted.items()[:num_closest]})
    print('\nPredicted label: %0.2f' % predicted_label)