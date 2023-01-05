# Dictionaries

## Manual
* [Manual (XML)](https://github.com/petermr/semanticClimate/blob/main/ipcc/ar6/wg3/Chapter03/dict/manual_dict_chapter03.xml)

## Abbreviation
* [Abbreviations (XML)](https://github.com/petermr/semanticClimate/blob/main/ipcc/ar6/wg3/Chapter03/dict/abb_chapter03.xml)

## Keywords
* [Keywords/Phrases (CSV)](https://github.com/petermr/semanticClimate/blob/main/ipcc/ar6/wg3/Chapter03/dict/gensim_keywords.csv)

# How to generate your dictionaries:


1)**Manual dictionary:** Manually created by the chapter champions from reading the chapter and picking out words or bi-grams that are less frequently used or are difficult to understand in the context of the report. The dictionary needs to be in .xml format.

  
2)**Automated dictionary**: Automated created by docanalysis using the spacy method.
The abbreviation dictionary can be created by following the steps given below:

* mkdir wiki_hackathon

* cd wiki_hackathon

* mkdir Chapter03

* cd Chapter03

* mkdir sections

* cd sections

* mkdir 0_main_body

- Place the html of your chapter inside the 0_main_body directory.

```docanalysis --project_name wiki_hackathon --output dict_search_5.csv --make_json dict_search_5.json --make_ami_dict entities --extract_abb ip_3_3_urban_abb```

where,

--project name – the name of the project (here, wiki_hackathon)

--output - a csv for dictionary search (not of our use, but required to be created)

--make_json - just enter this. Not of current use, but required.

--make_ami_dict – uses the entities created in the above command

--extract_abb - the abbreviation dictionary that is the output.
