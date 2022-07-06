# semanticClimate
Conversion of IPCC documents into semantic form


## goals

* to convert the IPCC documents from PDF into (a) HTML (b) XML
* extract terms and exploire their use and meaning
* link terms to Wikidata and create AMI-dictionaries
* create new structiures for navigation, search, display

# Content

Initially we will start with AR6 WGIII but move onto other WG's and perhaps look backwards as well.

## Strategy

* Create a directory ("CProject") with all current PDFs (Chapters, etc.)
Location: https://github.com/petermr/semanticClimate/ipcc

Download components, using a hierarchical naming scheme, and convert to text (`pdf2txt`)

```
semanticClimate pm286$ cd ipcc/ar6/wg3/
$ ls
Chapter01.pdf
$ mkdir Chapter01
$ cp Chapter01.pdf Chapter01/fulltext.pdf
$ cd Chapter01
$ pdf2txt.py -o fulltext.txt fulltext.pdf 
$ ls
fulltext.pdf	fulltext.txt
```
If you do not get `fulltext.txt` after running the `ls` command then, install `pdfminer.six` and execute the following commads in the Command Prompt:

```
cd pdfminer.six
python tools/pdf2txt.py "Copy path.pdf" -o "Copy path.txt"
```


