import pandas as pd	
from sklearn.feature_extraction.text import TfidfVectorizer


with open('exec03.txt') as f:
    lines = f.readlines()

new_lst = [x[:-1] for x in lines]
#print(new_lst)

new_list = []
for x in new_lst:
    if x != '':
        new_list.append(x)
print(len(new_list))

def stopwords():
    








corpus = new_list

tr_idf_model  = TfidfVectorizer()
tf_idf_vector = tr_idf_model.fit_transform(corpus)

tf_idf_array = tf_idf_vector.toarray()

words_set = tr_idf_model.get_feature_names_out()

df_tf_idf = pd.DataFrame(tf_idf_array, columns = words_set)

print(df_tf_idf)

df_tf_idf.to_csv("test.csv") 