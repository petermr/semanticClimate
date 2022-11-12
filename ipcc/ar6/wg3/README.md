# WG3 (Mitigation)

(description)
# The Climate Knowledge Hunt Hackathon
Our current Wiki Hackathon is a project that aims to perform text and data mining on IPCC report of 2021 (a global climate report) to extract knowledge using tools that are created by us, and helps us save time, and gain meaningful insights by performing several analysis. On a document that has 10,000 pages and several 100 digrams and tables, extracting meaning can be daunting. But not, if the machines do the reading of the document for us. And not just reading, but also sectioning it into images, tables and chapter subsections. And not just this, but analysing the text for us, and sending us the analysis in a way that can be understood by us, and meaningful knowledge extracted out of the document. And the time it takes for a machine to do it? It definitely less that reading the entire document. In fact, if the tools are installed properly, and run in the right way, we can have meaning from 10,000 pages in mere hours, or even an hour.
### We are currently using following tools
* PYAMI 
* DOCANALYSIS
* gensim(keyword extraction)

**PYAMI has been used for**:
* Converting pdf to html
* Validating whether the created dictionary is correct or not
* Annotating the dictionary, which means, one can find the word from the dictionary in the generated html file, and then go to the wikidata page for the word, just by clicking on the word.

**DOCANALYSIS has been used for**:
* Creating automated dictionary from a html file.
* Creating different entity dictionaries (abbreviation dictionary, organisation dictionary etc) from the same html file.

## THE PROTOCOL:
### Download the IPCC/ar6/wg3 Chapter* pdf: 
* [from IPCC website](https://www.ipcc.ch/report/ar6/wg3/)
* [from Peter’s github repository](https://github.com/petermr/semanticClimate/tree/main/ipcc/ar6/wg3) 
### Download Peter’s semanticClimate github repository:

 ``` git clone https://github.com/petermr/semanticClimate.git```
  
### Converting a pdf into html (we use pyami from Peter’s repository)
* Download pyami repository:
-  git clone the latest pyami from Peter’s repository

 ``` git clone https://github.com/petermr/pyami.git ```
 - Then enter inside pyami directory:

``` cd /some/where/pyami```
* Convert pdf to html:
- Use following command for pdf to html conversion:

``` python -m py4ami.ami_pdf --inpath /users/….../ipcc/ar6/wg3/Chapter*/Chapter.pdf --outdir /users/….../ipcc/ar6/wg3/Chapter*/ --maxpage 100```

where,
- inpath: path of the pdf file inside your machine
- outdir: path of the directory inside which the converted html will be saved
- maxpage: number of pages of the pdf that should be converted into html

**DICTIONARY**
#### Create manual dictionary from pdf:
This is done by manually reading the pdf, and manually entering any term or abbreviaion that you do not understand, or you think is important for the chapter. The dictionary is a xml file(emissions.xml).
* Use pycharm or a similar IDE environment that can be used to
- make dictionaries(manual dictionary)
- identify the problems in the dictionary 
- upload the changes made in the dictionary or other texts in Peter’s github
#### Create automated dictionary from html
- Docanalysis installation:
- Create a separate directory
``` mkdir /user/.../docanalysis```
- Run the following installation command:
``` pip install docanalysis```
- Test if installation is successful using the following command:
``` docanalysis –help```
- If the tool is successfully installed, perform following commands:
``` pwd```
- After placing it, use ``` pwd```
- the result should be

``` /user/…./docanalysis/wiki_hackathon/Chapter02/sections/0_main_body/```

Place the html of your chapter inside the 0_main_body directory repository.
* run the following command: 
 
 ``` docanalysis --project_name wiki_hackathon --output entities.csv --make_ami_dict entities.xml```
* run the following command, which creates the abbreviation dictionary:

``` docanalysis --project_name wiki_hackathon --output dict_search_5.csv --make_json dict_search_5.json --make_ami_dict entities --extract_abbemissions_abb```
- Making automated dictionaries other than abbreviation dictionary using docanalysis:

**ORGANISATION DICTIONARY**:

``` docanalysis --project_name wiki_hackathon --spacy_model spacy --entities ORG --output org.csv```

``` docanalysis --project_name wiki_hackathon --spacy_model spacy --entities ORG --output org_aut_aff.csvv --make_ami_dict org```

One can create other dictionaries as well, as described in the github page for docanalysis.   
[docanalysis page](https://github.com/petermr/docanalysis/blob/main/README.md)

**Validating the created dictionary:**

``` python -m py4ami.pyamix DICT --dict /Users/pm286/projects/semanticClimate/ipcc//ar6/wg3/Chapter02/dict/emissions.xml –valid```

**Annotating the created dictionaries:**
* install the py4ami using following command:

``` pip install py4ami```

* use the following command for annotation:

``` py4ami HTML --annotate --dict /Users/..../projects/semanticClimate/ipcc/ar6/wg3/Chapter02/dict/emissions.xml \
--inpath/Users/..../projects/semanticClimate/ipcc/ar6/wg3/Chapter02/fulltext.html \
--outpath/Users/..../projects/semanticClimate/ipcc/ar6/wg3/Chapter02/annotated/fulltext_emissions.html --color YELLOW```

## Chapters
* Chapter01
* [Chapter02 (Emissions)](Chapter02/README.md)
* [Chapter03]
* [Chapter04 (Mid-term)](Chapter04/README.md)
* [Chapter07 (Agriculture/AFOLU)](Chapter07/README.md)
* [chapter08 (urban)](chapter08/README.md)
