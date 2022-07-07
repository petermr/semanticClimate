def cap_separator(address: str):
    """
    Function to separate the caption from normal text of the image.
    """
    d = {'normal':[], 'caption':[]}
    flag = 0
    with open(address, 'r') as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                if word == "Figure":
                    flag = 1
                if flag == 1:
                    d['caption'].append(word)
                else:
                    d['normal'].append(word)


    lst = string_combiner(d)
    file_writer(lst, address)


def string_combiner(separated_dictionary) -> list:
    img_text = ''
    caption_text = ''
    for i in separated_dictionary['caption']:
        caption_text = caption_text + i + ' '
    for j in separated_dictionary['normal']:
        img_text = img_text + j + ' '
    return [img_text, caption_text]



def file_writer(content: list, address:str):
    name = address.split('.')[0]
    path = name + "separate_text.txt"
    with open(path, 'w') as fp:
        for item in content:
            # write each item on a new line
            fp.write("%s\n" % item)
