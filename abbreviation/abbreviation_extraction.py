import spacy
import scispacy
from bs4 import BeautifulSoup
from abbreviations import schwartz_hearst
from scispacy.abbreviation import AbbreviationDetector
from IPython.display import HTML
import pandas as pd
import requests
import os
import argparse


class abbreviation_extraction():
  def __init__(self, html_path, saving_path, model, marker, save_text):
    self.html_path = html_path
    self.saving_path = saving_path
    self.dict_abbreviation = {}
    self.dict_abbreviation_swartz = {}
    self.model = model
    self.save_text = save_text
    self.text = ''
    self.marker = marker

  def make_clickable(val):
          #print(type(val))
          l = [f'<a target="_blank" href="{val_}">{val_}</a>' for val_ in val]
          return l
  def wikidata_lookup(self, row):
          query = row['long_form']
          #print('query',query)
          params	= {
                  "action"		: "wbsearchentities",
                  "search"		: query,
                  "language"	: "en",
                  "format"		: "json"
                }
          data	= requests.get("https://www.wikidata.org/w/api.php",params=params)
          result = data.json()
          hit_list = []
          for hit in result['search']:
            try:
              if "scientific article" not in hit["description"]:
                  hit_list.append(hit["url"])
            except:
                  hit_list.append(hit["url"])
          return hit_list
  
  def text_extraction(self):
    with open(self.html_path, 'r') as f:
      html = f.read()
      soup = BeautifulSoup(html, features="html.parser")

      # kill all script and style elements
      for script in soup(["script", "style"]):
          script.extract()    # rip it out

      # get text
      text = soup.get_text()

      # break into lines and remove leading and trailing space on each
      lines = (line.strip() for line in text.splitlines())
      # break multi-headlines into a line each
      chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
      # drop blank lines
      #text_write = '\n'.join(chunk for chunk in chunks if chunk)
      self.text = '\n'.join(chunk for chunk in chunks if chunk)
      #print(text)
    return self.text

  def scispacy_extraction(self, doc):
    for abrv in doc._.abbreviations:
        new_dict  ={}
        abrv_ = str(abrv)
        long_f = str(abrv._.long_form)
        if '(' in  long_f or ')' in long_f or abrv_ == long_f or abrv_ == long_f +'s':
            continue
        else:  
            if abrv_ not in self.dict_abbreviation:
              new_dict['long_form']= abrv._.long_form
              new_dict['count'] = int(1)
              self.dict_abbreviation[str(abrv)] = new_dict  
            else:  
              self.dict_abbreviation[str(abrv)]['count'] = int(self.dict_abbreviation[str(abrv)]['count'])+ 1
              continue
    return self.dict_abbreviation

  def dict_extraction_swartz(self, pairs):
    for key, value in pairs.items():
    
      new_dict  ={}
      abrv_ = key
      long_f = value
      
      if '(' in  long_f or ')' in long_f or abrv_ == long_f or abrv_ == long_f +'s':
          continue
      else:  
          if abrv_ not in self.dict_abbreviation_swartz:
            new_dict['long_form']= long_f
            new_dict['count'] = int(1)
            self.dict_abbreviation_swartz[str(abrv_)] = new_dict  
          else:  
            self.dict_abbreviation_swartz[str(abrv_)]['count'] = int(self.dict_abbreviation_swartz[str(abrv_)]['count'])+ 1
            continue
    return self.dict_abbreviation_swartz  
  
  def table_generation(self, dictionary_abbreviation,CSV_SAVE_PATH):
        #CSV_SAVE_PATH = self.saving_path + 'abbreviation_table_.csv'
        entry = {'abbreviation':[''],'long_form':[''],'count':[0],'marker':['']}
        df = pd.DataFrame(entry)
        for l in dictionary_abbreviation:
          #print(l)
          entry = {'abbreviation':str(l),'long_form':str(dictionary_abbreviation[l]['long_form']),'count':dictionary_abbreviation[l]['count'],'marker':self.marker}
          df = df.append(entry, ignore_index= True)
        df = df.drop(0)
        df = df.reset_index(drop=True)
        df_copy = df.copy()
        #print(df) 

        df['wiki_search_links'] = df.apply(lambda row: self.wikidata_lookup(row), axis =1)
        

        df.style.format({'wiki_search_links': self.make_clickable})      
        df.to_csv(CSV_SAVE_PATH, index = None)
  
  def main(self):
      
      if not os.path.exists(self.saving_path):
        os.makedirs(self.saving_path) 
      
      text = self.text_extraction()
      
      
      
      TEXT_ = f'Chapter_text.txt'
      DICTIONARY_SH = f'Chapter_dictionary_SH.txt'
      DICTIONARY_Spacy= f'Chapter_dictionary_Spacy.txt'
      if self.save_text:
        with open(self.saving_path + TEXT_, 'w') as file:
            file.write(text)
      
      
      if self.model == 'spacy':
        nlp = spacy.load('en_core_web_sm')
        abbreviation_pipe = AbbreviationDetector(nlp)
        nlp.add_pipe(abbreviation_pipe)
        doc = nlp(text)
        self.scispacy_extraction(doc)
        dictionary_abbreviation = self.dict_abbreviation
        CSV_SAVE_PATH = self.saving_path + 'abbreviation_table_spacy.csv'
        # with open(self.saving_path + DICTIONARY_Spacy, 'w') as file:
        #     for abrv in doc._.abbreviations:
              
        #       #print(abrv ,abrv._.long_form)
        #       #print(key, value )
        #       file.write('{'+str(abrv)+' : '+ str(abrv._.long_form)+"}")  
        #       file.write('\n')

      elif self.model == 'swartz':
        pairs = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text= text)
        #print('pairs',pairs)
        self.dict_extraction_swartz(pairs)
        dictionary_abbreviation = self.dict_abbreviation_swartz
        CSV_SAVE_PATH = self.saving_path + 'abbreviation_table_swartz.csv'
        # with open(self.saving_path + DICTIONARY_SH, 'w') as file:
        #     for key, value in pairs.items():
        #       #print(key, value )
        #       file.write('{'+str(key)+' : '+ str(value)+"}")
        #       file.write('\n')
      
      elif self.model == 'both':
        
        pairs = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text= text)
        self.dict_extraction_swartz(pairs)

        nlp = spacy.load('en_core_web_sm')
        abbreviation_pipe = AbbreviationDetector(nlp)
        nlp.add_pipe(abbreviation_pipe)
        doc = nlp(text)
        self.scispacy_extraction(doc)
        dictionary_abbreviation_spacy = self.dict_abbreviation
        #print(dictionary_abbreviation_spacy)
        dictionary_abbreviation_swartz = self.dict_abbreviation_swartz
        dictionary_abbreviation = dict(dictionary_abbreviation_swartz, **dictionary_abbreviation_spacy)
        #print(dictionary_abbreviation)
        CSV_SAVE_PATH = self.saving_path + 'abbreviation_table_both.csv'


      self.table_generation(dictionary_abbreviation,CSV_SAVE_PATH)
      
      #return df




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--html_path',
                      required=True,
                      help='give the path where your html lives: /...')
    parser.add_argument('--saving_path',
                      required=True,
                      help='path of the folder where you want to save the files : /...'
                      )
    parser.add_argument('--model',
                      required=True,  choices=['swartz','spacy','both'],
                      help='which model you want to us to extact abbreviations /...')
    parser.add_argument('--marker',
                      required=True,
                      help='give identifier for that input file ex: Chapter_no_6 etc : /...'
                      )                  
    parser.add_argument("-t", help="save text",
                        action="store_true")

    args = parser.parse_args()

    html_path = args.html_path #'/content/semanticClimate/ipcc/ar6/wg3/Chapter06/fulltext.flow.html'
    saving_path = args.saving_path  #'/content/'
    model = args.model
    save_text = args.t
    marker = args.marker
    abbreviation = abbreviation_extraction(html_path, saving_path, model,marker,save_text)
    
    abbreviation.main()
    

