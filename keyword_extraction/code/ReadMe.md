# Keyword Extraction

### **Input**
 We are using html as input file 

### **Output** 
As result we get text file we will use that text file for getting keywords and keyphrases
  
## **Usage (CLI only)**

    keyword_extraction.py --help  
    
    usage: keyword_extraction_v2_test.py [-h] --html_path HTML_PATH --saving_path SAVING_PATH
                                     [--method {rake,yake,gensim,keyBERT,textrank,rawtext}] [--n_gram N_GRAM]
                                     [--html2text]

    optional arguments:
    -h, --help            show this help message and exit
    --html_path HTML_PATH
                          give the path where your html lives: /...
    --saving_path SAVING_PATH
                          path of the folder where you want to save the files : /...
                          
    --method {rake,yake,gensim,keyBERT,textrank,rawtext}
                          which method you want to us to extact keywords /...
                          
    --n_gram N_GRAM       length of n-grams to extract(Yake only) : /...
    --html2text           Converts HTML to TXT : /...

**Example Command To Extract Keywords**
    
    python keyword_extraction_v2_test.py --html_path semanticClimate\ipcc\ar6\wg3\Chapter05\fulltext.html --saving_path semanticClimate\ipcc\ar6\wg3\Chapter05\fulltext.html --method gensim
 
 * This will give us an output file called ```gensim_keywords.csv``` in the ```--saving_path``` directory
 * Replace the ```--html_path``` and ```--saving_path``` with 

## Methods for keywords/keyphrases:
1) gensim
2) Rake
3) yake
4) keybert
5) TD-IDF (to be implemented)



