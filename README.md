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

For *rake_nltk* (another keyword extractor):
```bash
pip3 install rake_nltk
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
./convert_to_text.py --pdfs pdfs/ --txts txts/
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

I can create an index file (*index.pkl*) with:
```bash
./create_index.py index.pkl --txts txts/
```
and query (with queries stored in *queries.yaml*) with:
```bash
./query.py queries.yaml index.pkl
```
which gives me:
```bash
covid: [(6.94191921041655e-05, 'txts//outbreak-update-7.txt', 'covid'), (0.0004443634551284221, 'txts//children-36.txt', 'covid')]
corona: [(0.002717349750564567, 'txts//antimicrobial-Agents-Chemotherapy-2020.txt', 'coronavirus'), (0.005543175840332845, 'txts//children-corona.txt', 'coronavirus')]
venezuala: [(0.009458640249675531, 'txts//venezuelan_migrants.txt', 'venezuelan migrants')]
venezuela: [(0.008970008953965818, 'txts//venezuelan_migrants.txt', 'venezuelan migrants')]
medic: [(0.0015031011723993745, 'txts//hiv-drug-trial.txt', 'medical society'), (0.005073313181321498, 'txts//mitigate-spread.txt', 'median')]
hyperactive: [(0.05283157880395907, 'txts//children-36.txt', 'c-reactive')]
social: [(4.7374173566215475e-05, 'txts//social-distancing.txt', 'social distancing measures'), (0.006873273194797273, 'txts//hiv-drug-trial.txt', 'society')]
```

## Support
Python 3.5+
