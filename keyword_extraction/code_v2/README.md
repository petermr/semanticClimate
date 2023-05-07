## Keyword Extraction

Keyword Extraction is a python script used to extract important phrases and keywords from the text input provided.
* Currently it only takes html as input files.
* The output is a word list in the csv file format.

It is built on a Hugging Face Token Classifier Api trained on the KBIR Inspec Model.  
Details can be found [Here](https://huggingface.co/ml6team/keyphrase-extraction-kbir-inspec)

### How To Use

* A novice user can use the Google Colab Notebook [here](https://colab.research.google.com/drive/1bbY046IABIKUuzjwmi8MrkKnCSereZav#scrollTo=JWQaYYxR6PxN)
* This is a CLI based tool with a few options for advanced users familiar with running CLI tools.
* Example  
 ```  python keyword_extraction_v2_test.py -i Chapter05.html -s [path\to\save\file]  ```
* Arguments  
  ```-h, --help            show this help message and exit  
  -i HTML_PATH, --html_path HTML_PATH  
                        path of the HTML file: /...  
  -t TEXT_FILE, --text_file TEXT_FILE  
                        path to textfile: /...  
  -s SAVING_PATH, --saving_path SAVING_PATH  
                        path of the folder where you want to save the files : /...  
  -m {rake,yake,gensim,keyBERT,textrank,rawtext,hf},  
  --method {rake,yake,gensim,keyBERT,textrank,rawtext,hf}  
                        which method you want to us to extact keywords (Default is HF Model) /...  
  --n_gram N_GRAM       length of n-grams to extract(Yake only) : /...  
  --html2text           Converts HTML to TXT : /...```
