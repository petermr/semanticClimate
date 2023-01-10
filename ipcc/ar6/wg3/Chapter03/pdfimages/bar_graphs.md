# Bar graph images

This is a  project to extract complete numerical data *automatically* from pixel imgaes (PNGs). It is based on a successful projrct to extract data from various types of plot;
discussion thread: https://github.com/petermr/petermr/discussions/8 .
 (https://github.com/petermr/petermr/discussions/8#discussioncomment-2495899) where a CSV file is created from a plot. 
 
<img src="https://user-images.githubusercontent.com/733515/161443757-3d494b55-7cda-42e9-bb22-a0b097fbd667.png"></img>

We propose to do this for bar graphs such as 
<img src="https://github.com/petermr/semanticClimate/blob/main/ipcc/ar6/wg3/Chapter03/pdfimages/image.24.1.90_506.297_531.png"></img>. It involves OCR for the text and `py4ami/pyamiimage` for pixels2primitives.

Here are some examples from Chapter03 of IPCC/AR6/WG3 (probably 10% of all images in the chapter). Success here extends to a huge range of problems ffrom all fields of science.


# tractable

* bar graph (slanted x-labels): https://github.com/petermr/semanticClimate/blob/main/ipcc/ar6/wg3/Chapter03/pdfimages/image.24.1.90_506.297_531.png
* bar graph (slanted x-labels): https://github.com/petermr/semanticClimate/blob/main/ipcc/ar6/wg3/Chapter03/pdfimages/image.25.1.84_511.30_270.png
* bar graph (slanted x-labels): https://github.com/petermr/semanticClimate/blob/main/ipcc/ar6/wg3/Chapter03/pdfimages/image.26.1.76_520.136_386.png
* multiple bar charts: https://github.com/petermr/semanticClimate/blob/main/ipcc/ar6/wg3/Chapter03/pdfimages/image.56.1.72_523.471_672.png
* multiple bar charts: https://github.com/petermr/semanticClimate/blob/main/ipcc/ar6/wg3/Chapter03/pdfimages/image.57.1.72_523.30_231.png

## more ambitious

* multiple bar graph panels: https://github.com/petermr/semanticClimate/blob/main/ipcc/ar6/wg3/Chapter03/pdfimages/image.27.1.72_539.195_445.png
* multi-multiple bar graph panels: https://github.com/petermr/semanticClimate/blob/main/ipcc/ar6/wg3/Chapter03/pdfimages/image.98.2.109_486.340_675.png

