import os
from SeparateCaption import *
#example of input and output directory in my machine
#input_dir = '/Users/kaartik/Desktop/images'
#output_dir = '/Users/kaartik/Desktop/output'

def text_extraction(file_address: str):

        name = file_address.split('.')[0]

        # if the output path is not there, create it
        path = name + '.txt'

        os.system(f'pyamiimage -t {file_address} {path}')
        cap_separator(path)

