#!/usr/bin/env python3

# External dependencies.
import os
from sortedcontainers import SortedList, SortedDict
import argparse
import pickle

# Internal dependencies.
from get_keywords import get_keyword_extractor

if __name__ == "__main__":

    # Parse command-line options.
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('index_file',
                        help='PKL file to save the index to.')
    parser.add_argument('--txts', dest='txtsdir', default='txts/',
                        help='Directory where text files are present.')
    parser.add_argument('-n', dest='num_keywords', default=20, type=int,
                        help='Number of keywords to extract.')
    parser.add_argument('--alg', dest='algorithm', default='yake', choices=('rake', 'yake'),
                        help='Keyword extraction algorithm to use.')
    args = vars(parser.parse_args())

    # Our index is a sorted dictionary of keywords.
    # Each keyword is mapped to a sorted list (according to scores).
    index = SortedDict()

    # Load path.
    TXTS_DIR = args['txtsdir']
    documents = os.listdir(TXTS_DIR)

    # Load keyword extraction algorithm.
    algorithm = args['algorithm']
    keywords = get_keyword_extractor(algorithm)
    
    # Number of keywords per document.
    num_keywords_per_document = args['num_keywords']
    
    for document in documents:
        document_full_path = TXTS_DIR + '/' + document
        doc_keywords = keywords(document_full_path, num_keywords_per_document)
        for keyword, score in doc_keywords:
            if keyword not in index:
                index[keyword] = SortedList()
            index[keyword].add((score, document_full_path))

    index_file = args['index_file']
    with open(index_file, 'wb') as f: 
        pickle.dump(index, f, pickle.HIGHEST_PROTOCOL)