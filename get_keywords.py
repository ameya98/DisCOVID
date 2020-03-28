#!/usr/bin/env python3

import os
import argparse
import yake

# Parse command-line options.
parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument('text_file',
                    help='Text file to extract keywords from.')
parser.add_argument('-n', dest='num_keywords', default=20, type=int,
                    help='Number of keywords to extract.')
args = vars(parser.parse_args())

# Read text file.
text_file = args['text_file']
with open(text_file, 'r') as f:
    text = f.read()

# Extract keywords with YAKE.
num_keywords = args['num_keywords']
kw_extractor = yake.KeywordExtractor(dedupLim=0.9, dedupFunc='jaro', top=num_keywords)
keywords = kw_extractor.extract_keywords(text)

# Lower the score, more the relevance.
keywords = sorted(keywords, key=lambda pair: pair[1])

for kw_pair in keywords:
    keyword, score = kw_pair
    print("%0.4f: %s" % (score, keyword))