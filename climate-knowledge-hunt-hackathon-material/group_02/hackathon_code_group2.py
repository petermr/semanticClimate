from lxml import html
import requests
page = requests.get('https://raw.githubusercontent.com/petermr/semanticClimate/main/ipcc/ar6/syr/lr/total_pages_groups_confidence.html')
tree = html.fromstring(page.content)
paragraphs = tree.xpath('/html/body/div[1]/div[16]')
for paragraph in paragraphs:
    print(f' text: {str(list(paragraph.itertext()))}')