import pandas as pd
import re
import numpy as np
import xmltodict
import tqdm
import xml.etree.ElementTree as ET

def keyphras():
    keyphrases = pd.read_csv('Chapter05_keyphrases.csv')



    root = ET.parse("ip_3_5_man.xml")
    terms = []
    for entry in root.findall('.//entry'):
        term = entry.get('term')
        terms.append(term.lower())

    keyList = keyphrases['0'].tolist()
    keylist2 = []
    for i in keyList:
        keylist2.append(i.lower())

    common_el = set(keylist2) & set(terms)
    print(len(common_el))

def extraction_unigrams():

    df = pd.read_csv('Chapter05_keyphrases.csv')
    key = df['0'].tolist()
    unigram =[]
    ngram = []

    pattern = "\s"
    print(type(key))
    for i in key:
        if re.findall(pattern, i):
            ngram.append(i)
            #print('N-gram')
        else:
            unigram.append(i)
            #print('Unigram')
    #print(ngram)
    print(unigram)
    print(len(unigram))
    #print(len(ngram))
        
        
            
'''        else:
            print('Unigram')'''
    
    



extraction_unigrams()

#print(terms)
#print(keyphrases.to_string())



