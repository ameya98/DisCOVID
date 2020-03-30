#!/usr/bin/env python3

import os
import numpy as np

with open('txts/fake-news-collection.txt', 'r') as f:
    lines = list(f.readlines())
    curr_doc_index = 0
    curr_doc = []
    for index, line in enumerate(lines):
        if line.strip() != '':
            curr_doc.append(line)
        else:
            if len(curr_doc) != 0:
                with open('txts/fake-news-split-%d.txt' % curr_doc_index, 'w') as curr_f:
                    curr_f.writelines(curr_doc)
                    print(curr_doc_index, curr_doc)
                print("\n")
                curr_doc = []
                curr_doc_index += 1