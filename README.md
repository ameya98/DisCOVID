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

## Usage
To convert PDF files:
```bash
./convert_to_text.py --pdfs pdf-dir --txts text-dir
```
where *pdf-dir* and *text-dir* are the input and output directories.

Once the PDF files are converted to text, extract keywords with:
```bash
./get_keywords.py txt-file -n num-keywords
```
which outputs keywords and scores, in order of increasing relevance.

## Support
Python 3.5+