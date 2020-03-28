#!/usr/bin/env python3

# External dependencies.
import os
from sortedcontainers import SortedList, SortedDict
import argparse
import pickle
import yaml
import numpy as np

# For string similarity.
from strsimpy.normalized_levenshtein import NormalizedLevenshtein
from strsimpy.jaro_winkler import JaroWinkler


# Returns 1 iff s1 == s2, else 0.
def exact_similarity(s1, s2):
    if s1 == s2:
        return 1
    else:
        return 0


# Returns a function for the chosen similarity measure.
def similarity_function(similarity_measure):
    if similarity_measure == 'exact':
        return exact_similarity
    elif similarity_measure == 'nlevs':
        return NormalizedLevenshtein().distance
    elif similarity_measure == 'jaro':
        return JaroWinkler().similarity
    else:
        raise ValueError('Invalid similarity measure.')


if __name__ == "__main__":

    # Parse command-line options.
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('query_file',
                        help='YAML file which contains the queries.')
    parser.add_argument('index_file',
                        help='PKL file which contains the index.')
    parser.add_argument('--sim', dest='similarity_measure', default='jaro', choices=('exact', 'nlevs', 'jaro'),
                        help='Choice of similarity metric.')
    parser.add_argument('-n', dest='num_files_per_query', default=2, type=int,
                        help='Number of relevant files to return for each query.')
    parser.add_argument('--thres', dest='similarity_threshold', default=0.8, type=float,
                        help='Similarity threshold, between 0 and 1. Will not select keywords with similarity to the query lower than this.')

    args = vars(parser.parse_args())

    # Load queries.
    query_file = args['query_file']
    with open(query_file, 'r') as f:
        queries = yaml.safe_load(f)
    
    # Load index.
    index_file = args['index_file']
    with open(index_file, 'rb') as f:
        index = pickle.load(f)
    
    # Load similarity function.
    similarity_measure = args['similarity_measure']
    similarity = similarity_function(similarity_measure)

    # Search index.
    similarity_threshold = args['similarity_threshold']
    num_files_per_query = args['num_files_per_query']
    for query in queries:
        results = []
        for indexed_keyword, indexed_entries in index.items():
            for score, doc in indexed_entries:
                curr_similarity = similarity(query, indexed_keyword)
                if curr_similarity >= similarity_threshold:
                    score *= np.exp(-curr_similarity)
                    results.append((score, doc, indexed_keyword))
    
        print("%s: %s" % (query, sorted(results)[:num_files_per_query]))