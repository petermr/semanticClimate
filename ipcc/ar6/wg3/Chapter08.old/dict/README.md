# Dictionary: Collection of words and their meanings
Types of Dictionary 
1) ip_3_8_urban_man.xml(Manual dictionary)
2) ip_3_8_urban_abb.xml(Automated dictionary)

1)**Manual dictionary:** Manually created by the chapter champions from chapter reading having most of the terms that are important for chapter and difficult to understand.
It's in .XML format

  
2)**Automated dictionary**: Automated created by docanalysis using spacy. 
**method:**
  * mkdir wiki_hackathon

* cd wiki_hackathon

* mkdir Chapter08

* cd Chapter08

* mkdir sections

* cd sections

* mkdir 0_main_body

- Place the html of your chapter inside the 0_main_body directory.

```docanalysis --project_name wiki_hackathon --output dict_search_5.csv --make_json dict_search_5.json --make_ami_dict entities --extract_abb ip_3_8_urban_abb```

where,

--project name – the name of the project (here, wiki_hackathon)

--output - a csv for dictionary search (not of our use, but required to be created)

--make_json - just enter this. Not of current use, but required.

--make_ami_dict – uses the entities created in the above command

--extract_abb - the abbreviation dictionary that is the output.



