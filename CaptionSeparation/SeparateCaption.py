def cap_separator(address: str) -> list:
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

    return string_combiner(d)

def string_combiner(separated_dictionary) -> list:
    img_text = ''
    caption_text = ''
    for i in separated_dictionary['caption']:
        caption_text = caption_text + i + ' '
    for j in separated_dictionary['normal']:
        img_text = img_text + j + ' '
    return [img_text, caption_text]




