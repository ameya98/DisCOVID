#!/usr/bin/env python3

import os
import numpy
import argparse
import yaml

if __name__ == "__main__":

    # Parse command-line options.
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('labels_file', default='labels.yaml',
                        help='YAML labels file for output.')
    parser.add_argument('txtsdir', default='txts/',
                        help='Directory where to load corresponding text files.')
    args = vars(parser.parse_args())

    # Hardcoded rules for fake vs real.
    def fake(file_name):
        if file_name[:4] == 'fake':
            print('Marked as fake: %s' % file_name)
            return True
        else:
            return False
    
    # Iterate through dir
    dir = os.listdir(args['txtsdir'])
    labels = {}
    for curr_file in dir:
        labels[args['txtsdir'] + '/' + curr_file] = fake(curr_file)


    print('\n Labels: \n %s' % labels)
    with open(args['labels_file'], 'w') as f:
        yaml.dump(labels, f)


