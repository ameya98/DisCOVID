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
```
pip3 install sortedcontainers
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
