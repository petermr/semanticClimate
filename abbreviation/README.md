   **Abbreviation Extraction**
##

This folder contains all the codes and the outcomes of the different methodology used for extracting Abbreviation from HTML and their full forms.
The dataset used for abbreviation extraction task can be found in [here](https://github.com/petermr/pyami/tree/main/temp/html) which consists of the starting 300 pages of the Climate Report. 
**Dataset Link**: https://github.com/petermr/pyami/tree/main/temp/html

The code which I have used to extract abbreviations from the HTML files can be found in the link below:
https://github.com/ananyas168/petermr/blob/main/climate_abbreviation_extraction.ipynb

 The idea behind the code is as follows:

- Convert an HTML to raw text using BeautifulSoup.

- Extracting abbreviations using the NLP tool based on the [Schwartz-Hearst algorithm](https://psb.stanford.edu/psb-online/proceedings/psb03/schwartz.pdf). ( Here is the link for the tool: https://github.com/philgooch/abbreviation-extraction/blob/develop/README.md) and using scispacy abbreviation extractor

- Saving the extracted raw text and the abbreviations in txt format.
- Creating a final table with abbreviation, longform, count and wiki_lookup links in it.(see the image below for reference)
![image](https://user-images.githubusercontent.com/66965350/176549219-bcbd726d-2dbf-4787-90a7-be87ae4bdc6f.png)




The structure of the folder is explained below:
- Subfolder:**Codes** contains the ipynb file of the code which is used for extracting the abbreviation in the above mentioned methodology.
- Subfolder: **Pages** contains the extracted raw text from HTML and the abbreviations in respective txt files.



Inside Subfolder **Pages** there are subsubfolder named as **page_X**, where X stands for the page noumber.
And Inside this subsubfolder you can find three .txt files, namely:
- page_X_dictionary_SH.txt  -->  contains the abbreviation extracted using [Schwartz-Hearst algorithm](https://psb.stanford.edu/psb-online/proceedings/psb03/schwartz.pdf).

- page_X_dictionary_Spacy.txt -->  contains the abbreviation extracted scispacy abbreviation extractor.

- page_X_text.txt           -->   contains the raw text extracted by BeutifulSoup from HTML.

where X represents the page number. 

The final output is presentin the parent folder with the name **abbreviation_table.csv** in a csv ormat which represents the our output formation aftter running through the code(an easy to read and access format in csv).
