import pickle
import json
from wordcloud import WordCloud
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import argparse
def word_cloud(file_path,saving_path,chp_name):
  file_path = file_path +'word_cloud_data_chapter.json'
  with open(file_path,'r') as f:
    tf_idf_dict = json.load(f)

  # for chp_name in tf_idf_dict.keys()
  wordcloud = WordCloud(background_color="white").generate_from_frequencies(tf_idf_dict[chp_name]) 
  fig = plt.figure(figsize=(13,9))
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis("off")
  plt.show()
  fig.show()
  fig.savefig(saving_path+ f'/{chp_name}_word_cloud.jpg', bbox_inches='tight', dpi=150)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path',
                      required=True,
                      help='give the path of the folder where your json file resides: /...')
    parser.add_argument('--saving_path',
                      required=True,
                      help='path of the folder where you want to save the files : /...'
                      )
    parser.add_argument('--Chapter_name',
                      required=True,  choices=['Chapter02', 'Chapter08', 'Chapter04', 'Chapter07', 'Chapter15', 'Chapter16', 'Chapter01', 'Chapter17'],
                      help='which chapter you are interested in /...')
    

    args = parser.parse_args()

    file_path = args.file_path 
    Chapter_name = args.Chapter_name
    saving_path = args.saving_path
    
    word_cloud(file_path,saving_path,Chapter_name)
