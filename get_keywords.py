#!/usr/bin/env python3

import os
import argparse
import numpy as np
import yake
import rake_nltk
    
# Returns keyword extraction algorithm.
def get_keyword_extractor(algorithm):
    if algorithm == 'yake':
        return keywords_yake
    elif algorithm == 'rake':
        return keywords_rake

# Returns the most relevant keywords as a list of tuples (keyword, score). Lower the score, more relevant the keyword to this document.
def keywords_yake(text_file, num_keywords):

    # Read text file.
    with open(text_file, 'r') as f:
        text = f.read()

    # Extract keywords with YAKE.
    kw_extractor = yake.KeywordExtractor(dedupLim=0.9, dedupFunc='seqm', top=num_keywords)
    keywords = kw_extractor.extract_keywords(text)

    # Lower the score, more the relevance.
    keywords = sorted(keywords, key=lambda pair: pair[1])
    return keywords

# Returns the most relevant keywords as a list of tuples (keyword, score). Lower the score, more relevant the keyword to this document.
def keywords_rake(text_file, num_keywords):

    # Read text file.
    with open(text_file, 'r') as f:
        text = f.read()

    rake = rake_nltk.Rake()

    # Extraction given the text.
    rake.extract_keywords_from_text(text)

    def no_numbers(phrase):
        for char in phrase:
            if char.isdigit():
                return False
        return True

    # To get keyword phrases ranked highest to lowest with scores.
    return [(keyword, np.exp(-score)) for (score, keyword) in rake.get_ranked_phrases_with_scores()[:num_keywords] if no_numbers(keyword)]

if __name__ == "__main__":

    # Parse command-line options.
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('text_file',
                        help='Text file to extract keywords from.')
    parser.add_argument('-n', dest='num_keywords', default=20, type=int,
                        help='Number of keywords to extract.')
    parser.add_argument('--alg', dest='algorithm', default='yake', choices=('rake', 'yake'),
                        help='Keyword extraction algorithm to use.')
    args = vars(parser.parse_args())

    algorithm = args['algorithm']
    keywords = get_keyword_extractor(algorithm)

    # Obtain keywords and print along with score.
    doc_keywords = keywords(args['text_file'], args['num_keywords'])
    for kw_pair in doc_keywords:
        keyword, score = kw_pair
        print("%0.4f: %s" % (score, keyword))
