#!/usr/bin/env python3

import os
import argparse
import yake

# Returns the most relevant keywords as a list of tuples (keyword, score). Lower the score, more relevant the keyword to this document.
def keywords(text_file, num_keywords):

    # Read text file.
    with open(text_file, 'r') as f:
        text = f.read()

    # Extract keywords with YAKE.
    kw_extractor = yake.KeywordExtractor(dedupLim=0.9, dedupFunc='seqm', top=num_keywords)
    keywords = kw_extractor.extract_keywords(text)

    # Lower the score, more the relevance.
    keywords = sorted(keywords, key=lambda pair: pair[1])
    return keywords


if __name__ == "__main__":

    # Parse command-line options.
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('text_file',
                        help='Text file to extract keywords from.')
    parser.add_argument('-n', dest='num_keywords', default=20, type=int,
                        help='Number of keywords to extract.')
    args = vars(parser.parse_args())

    # Obtain keywords and print along with score.
    doc_keywords = keywords(**args)
    for kw_pair in doc_keywords:
        keyword, score = kw_pair
        print("%0.4f: %s" % (score, keyword))
