#!/usr/bin/env python3

import os
import argparse

# Parse command-line options.
parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
parser.add_argument('-f', '--force', default=False, action='store_true',
                    help='Regenerate text file even if it already exists.')
parser.add_argument('--pdfs', dest='pdfsdir', default='pdfs/',
                    help='Directory where PDFs are stored.')
parser.add_argument('--txts', dest='txtsdir', default='txts/',
                    help='Directory where to store corresponding text files.')
args = vars(parser.parse_args())

# Extract parameters
PDF_DIRECTORY = args['pdfsdir']
TEXT_DIRECTORY = args['txtsdir']
force = args['force']

# Check if output directory exists.
if not os.path.exists(TEXT_DIRECTORY):
    os.makedirs(TEXT_DIRECTORY)

# Convert PDFS one by one using pdftotext.
pdf_files = os.listdir(PDF_DIRECTORY)
for pdf_file in pdf_files:
    pdf_file_full_path = PDF_DIRECTORY + '/' + pdf_file
    
    text_file = pdf_file.replace('.pdf', '.txt')
    text_file_full_path = TEXT_DIRECTORY + '/' + text_file

    if force or not os.path.exists(text_file_full_path):
        os.system('pdftotext %s - > %s' % (pdf_file_full_path, text_file_full_path))
