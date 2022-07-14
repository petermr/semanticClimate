This file gives you a brief description on how to use abbreviation_extraction code on your html file.

Run the following commands in your terminal.

  
    !git clone https://github.com/petermr/semanticClimate.git
    
    %cd /content/semanticClimate/abbreviation/Codes/
    
    !pip install -r requirement.txt
    
    !python -m spacy download en_core_web_sm
  
    !python abbreviation_extraction.py --html_path [path to your html] --saving_path [path where you want to save the file] \
    --model [example : 'spacy' ] --marker [ some identifier you wanna add] -t
  
To better undertsand I have given an example run below:

    !python abbreviation_extraction.py --html_path /content/semanticClimate/ipcc/ar6/wg3/Chapter06/fulltext.flow.html --saving_path /content/ \
    --model 'both' --marker 'Chapter 6' -t


Once you run the above set of lines in your terminal you will get the abbreviation table in a csv format based on the the model type you choose:

 To understand the positional commands run the code below:
    
    !python abbreviation_extraction.py -h
 
 For better understnding I have attached the output of the above command line run, -h gives you description of the positional arguments.
 
     usage: abbreviation_extraction.py [-h] --html_path HTML_PATH --saving_path
                                  SAVING_PATH --model {swartz,spacy,both}
                                  --marker MARKER [-t]

      optional arguments:
        -h, --help            show this help message and exit
        --html_path HTML_PATH
                              give the path where your html lives: /...
        --saving_path SAVING_PATH
                              path of the folder where you want to save the files :
                              /...
        --model {swartz,spacy,both}
                              which model you want to us to extact abbreviations
                              /...
        --marker MARKER       give identifier for that input file ex: Chapter_no_6
                              etc : /...
        -t                    save text
