import numpy as np
from IPython.display import display
from IPython.display import clear_output,Markdown
import pandas as pd
import time
import pprint
import os

def wrapping_text_to_display(text):
  wrapped_text = pprint.pformat(text,width=50).replace("'","")
  if wrapped_text[0]=="(":
      wrapped_text = wrapped_text[1:]
  if wrapped_text[-1]==")":
      wrapped_text = wrapped_text[:-1]
  return wrapped_text


def Lets_Annotate(data_path):
  
  clear_output()
  
  path_save = "/content/drive/MyDrive/SemanticClimate_Hackathon_Annotation/"
  if not os.path.exists(path_save):
      os.makedirs(path_save)
      df = pd.read_csv(data_path)
      if "Annotation" not in df.columns:
          df["Annotation"] = np.NaN
          df.to_csv(os.path.join(path_save,"SemanticClimate_Annotations.csv"),index=None)
  else:
      df = pd.read_csv(os.path.join(path_save,"SemanticClimate_Annotations.csv"))
  df_= df.dropna(subset = ["Annotation"])
  anno_id = max(0,df_.shape[0])
  while(anno_id<df["Annotation"].shape[0]):
    # anno_id = min(0,df[df["Annotation"]!=np.NaN].shape[0])
    display(Markdown(f"**Sucessfully annotated samples: {anno_id}**"))
    display(Markdown("## Source Node:"))
    display(Markdown(f"####Name:"))
    display(Markdown(f"       {df['anchor_id'].iloc[anno_id]}"))
    display(Markdown(f"####Description:"))
    display(Markdown(f"              {wrapping_text_to_display(df['anchor_text'].iloc[anno_id])}"))
    display(Markdown(f"####Keywords:"))
    display(Markdown(f"             {df['anchor_keywords'].iloc[anno_id]}")) 
    display(Markdown(f"####Summary:"))
    display(Markdown(f"             {df['anchor_summary'].iloc[anno_id]}"))  
    display(Markdown("## Target Node:"))
    display(Markdown(f"####Name:"))
    display(Markdown(f"       {df['target_id'].iloc[anno_id]}"))
    # display(Markdown(f"Name:   {df['target'].iloc[anno_id]}"))
    display(Markdown(f"####Description:"))
    display(Markdown(f"              {wrapping_text_to_display(df['target_text'].iloc[anno_id])}"))
    display(Markdown(f"####Keywords:"))
    display(Markdown(f"             {df['target_keywords'].iloc[anno_id]}")) 
    display(Markdown(f"####Summary:"))
    display(Markdown(f"             {df['target_keywords'].iloc[anno_id]}"))
    display(Markdown("### Possible Type of relation between the source and the target Node:"))
    display(Markdown(f"         1 ->  Part of ,"))
    display(Markdown(f"         2 ->  Not Part of,"))
    display(Markdown(f"         3 ->  Inconclusive"))
    display(Markdown("#### Enter the relation Id between the source and the target Node (for example: Enter 1 if the target seems to be a part of source):"))
    relation_attribute = input()
    
    if len(relation_attribute)!=0:
        df.loc[anno_id, "Annotation"] =relation_attribute
        # display(Markdown("### Annotation:"))
        # display(Markdown(relation_attribute))
    else:
        df.iloc[anno_id]["Annotation"] ="skipped"
    df.to_csv(os.path.join(path_save,"SemanticClimate_Annotations.csv"),index=None)
    time.sleep(1)
    clear_output()
    anno_id+=1

