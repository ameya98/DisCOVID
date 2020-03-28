# DisCOVID
Team 88's repository for the JHU Design Challenge.

## Installation
Instructions are for an Ubuntu (16.04+) system.  
For *pdftotext*:
```bash
sudo apt install poppler-utils
```

For *yake* (from [official repository](https://github.com/LIAAD/yake)):
```bash
pip3 install git+https://github.com/LIAAD/yake
```

For *sortedcontainers* (for the index creation):
```bash
pip3 install sortedcontainers
```

For *yaml* and *strsimpy* (for the queries):
```bash
pip3 install PyYAML strsimpy
```

## Usage
Clone the repository, first!
```bash
git clone https://github.com/ameya98/DisCOVID.git
cd DisCOVID
```
To convert PDF files:
```bash
./convert_to_text.py --pdfs pdf-dir --txts text-dir
```
where *pdf-dir* and *text-dir* are the input and output directories.

Once the PDF files are converted to text, extract keywords from a text file with:
```bash
./get_keywords.py txt-file -n num-keywords
```
which outputs keywords and scores, in order of increasing relevance.

Create the index file (for a bunch of text files) with:
```bash
./create_index.py index-file --txts text-dir -n num-keywords
```
which creates a binary file storing the index.

Query the generated index file with queries stored in a YAML file:
```bash
./query_file.py query-file index-file
```
which outputs (score, document, keyword) pairs. Use the '-h' option, and see options for the similarity function (*'--sim'*) (supported options are: Normalized Leveshtein, Jaro-Winkler and Exact, all of which have range [0, 1].) and a threshold (*'--thres'*) which should also be in [0, 1].

## Examples
Running
```bash
./get_keywords.py txts/venezuelan_migrants.txt -n 10
```
gives me:
```bash
0.0220: venezuelan migrants
0.0226: world report venezuelan
0.0294: health
0.0379: venezuela
0.0410: report venezuelan migrants
0.0468: border
0.0503: march
0.0576: venezuelan ngo médicos
0.0579: migrants
0.0625: venezuelan health system
```

## Support
Python 3.5+
