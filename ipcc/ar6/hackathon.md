# Hackathon materials

2023-05-18 The HTML files have been automatically created from PDF files and are offered for re-use, e.g. by NLP and transformer tools. They are not free of errors but the rate is low and we believe good data can be obtained.

# Overview. 
The IPCC has published a series of reports which combined to create much of the SYR/Snthesis report. There are 6 apart from SYR. Read Wikpedia (https://en.wikipedia.org/wiki/Intergovernmental_Panel_on_Climate_Change) which includes this table

|Year|	Name of report|	Type of report|
|---|---|---|
|2023|	AR6 Synthesis Report: Climate Change 2023 (March 2023)|	Synthesis Report|
|2021 and 2022|	Sixth Assessment Report (AR6): Climate Change 2021: The Physical Science Basis (Working Group I, August 2021), 
Climate Change 2022: Impacts, Adaptation and Vulnerability (Working Group II, February 2022), 
|Mitigation of Climate Change (Working Group III, April 2022)|	Assessment Report (Working Group contributions)|
|2019|	Special Report on the Ocean and Cryosphere in a Changing Climate (SROCC)	|Special Report|
|2019|	Special Report on Climate Change and Land (SRCCL)|	Special Report

|2018|	Special Report on Global Warming of 1.5 °C (SR15)|	Special Report (

SYR is the start point, linking out to WGI, WGII, WGIII and SROCC, SRCCL and SR15. We'll mainly work with SYR and the 3 WGs.

## files and documents
Each report has several (large) PDF files an optionally some data. There are subreports , of each report, such as:
* SPM Summary for Policymakers
* TS Technical Summary
* LR Longer Report (SYR only)
* Chapters (WGI, WGII WGIII)

These have identifiers od the form <report> <subreport or chapter> <section> Example: `WGII SPM A.1.2.3`. Sections are number to 3 decimals and are explicit. We index to section level, and optionally to paragraphs where we append "a", "b" etc. In particular SYR/LR addresses other reports and sections in this manner. 
	
### floats
Much of the text is running/flowable, but interspersed with floats (figures, tables, boxes, etc.) . We renove these to the end of the document and will probably omit them in this hackathon. In principle, however we can make floats interactive and referenceable from the text

### hyperlinks
There are few clickable hyperlinks (probably onlt the TableOfContents (ToC)). We intend to add thousands more (initially cross references) to create a computable knowledge graph.

### annotations
The IPCC has meticulously added annotations such as *high confidence* . We extract these and make them semantic

## Structure
The directory has the top-level structure.
````
├── badlinks.txt
├── blog20230418pmr.md
├── copyright.md
├── editng_chapters.md
├── hackathon.md
├── intern_overview.md
├── sr15
│   ├── spm
│   └── ts_none
├── srccl
│   ├── spm
│   └── ts
├── srocc
│   ├── spm
│   └── ts
├── syr
│   ├── lr
│   └── spm
├── wg1
│   ├── spm
│   └── ts
├── wg2
│   ├── spm
│   └── ts
└── wg3
    ├── spm
    ├── structure.md
    └── ts
	````
within each report can be many more files. 
````
├── lr
│   ├── extract_floats.html
│   ├── fulltext.pdf
│   ├── pages
│   │   ├── page_1.html
│   │   ├── page_10.html
...
│   │   ├── page_85.html
│   │   ├── page_9.html
│   │   └── total_pages.html
│   ├── test_total_pages_groups.html
│   ├── total_pages.annotated.html
│   ├── total_pages.html
│   ├── total_pages.sections.html
│   ├── total_pages.sections_old.html
│   ├── total_pages_groups.html
│   ├── total_pages_groups_confidence.html
│   ├── total_pages_groups_table.csv
│   └── total_pages_section_3.html
└── spm
    ├── fulltext.pdf
    └── pages
        ├── page_1.html
        ├── page_10.html
        ├── page_11.html
        ├── page_12.html
...
        ├── page_8.html
        ├── page_9.html
        └── total_pages.html

````
The common components are:
* `fulltext.pdf` the raw file from IPCC
* `pages/` the immediate per-page output of `pdfplumber`. Note that raw output is not flowable
* `total-pages.html` The pages concatenated but still containing page breaks.

The toplevel files are very recent and not yet standardised. The latest are
* `total_pages_groups.html` where directories have been made hierarchical using the section decimal numbering. 
* total_pages_groups_confidence.html` includes annotations of confidence

* total_pages_groups_table.csv which is created for input to Wikidata

### manual edits and other software
WGIII (wg3) has been heavily worked on by interns and looks like:
````
    ├── Chapter01
    ├── Chapter01.pdf
    ├── Chapter02
	...

    ├── Chapter16
    ├── Chapter16.pdf
    ├── Chapter17
    ├── Chapter17.pdf
    ├── Dictionary
    ├── README.md
	
```
Within a typical chapter (e.g. 8, Urbanization) we can find

```
Chapter08
├── CompExecSumm.md
├── Document.rtf_bulleted_summary.pdf
├── FAQs.md
├── Introduction.md
├── README.md
├── SummForHSstudent.md
├── Updated_fulltext.pdf
├── Urban_Green_and_Blue_Infrastructure.png
├── annotated_fulltext_Chapter08.html
├── dict
│   ├── README.md
│   ├── ip_3_8_urban_abb.xml
│   └── ip_3_8_urban_man.xml
├── executive_summary.html
├── frequently_asked_questions.html
├── fulltext.html
├── fulltext.pdf
├── gensim_keywords.csv
├── images
│   └── fig_8_15.png
├── pdfimages
│   ├── image.13.1.72_523.30_217.png
│   ├── image.13.2.72_523.244_381.png
│   ├── image.14.1.72_524.30_435.png
...│
   ├── image.89.1.83_512.30_503.png
│   └── image.93.1.72_548.167_382.png
├── raw
│   ├── Rake_keywords.csv
│   ├── gensim_keywords.csv
│   └── yake_keywords.csv
├── table_of_contents.html
└── table_of_contents.md
````

(created by Priti Chahal). This includes dictionaries (dict/) and results of NLP tools (*.csv)