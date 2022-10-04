# OA Week hackathon 2022

Axel Duerkop suggested that the `semanticClimate` community creates an activity for OpenAccess week,
a global collection of activities related to OpenAccess (link to SPARC page). We propose a distributed,
asynchronous hack-project, based on the IPCC AR6 ClimateChange reports, with a tested modular structure
that is easy to take part in, contributes to global knowledge on climate and is inclusive. 
It's a great learning opportunity both for climate and OpenReading/OpenReuse technology.

# structure of IPCC and our motivation

The IPCC report is broken into 3 working groups (details), each of which has 15-20 Chapters. In total 
it's about 10,000 pages of PDF, difficult to read, even for experts and in a limited number of languages
(often only EN). There's a lot of Jargon, 15,000 references  which complicate reading and navigation is hard.
We can make this semantic (i.e. machines can understand it), so a wide variety of re-use is possible. 


# what #semanticClimate adds

Taking a Chapter, our (Open) tools convert it to HTML in smaller sections (e.g. Introduction, Sections, Executive summaries, 
Figure Captions, References). These can be studied individually or omitted (not everyone needs the References, 
some like to look at Figures). Then you can add meaning (ontology) through Wikidata (the Open collection of 100 million metadata
and data items). For example you can automatically find the named cities and do geocoordinate-based search and 
analysis, plot maps, etc.

The IPCC report contains huge amounts of useful data and metadata. It's often useful to "chunk" this, so we
can create a dictionary for each chapter (e.g. Emissions, Agriculture, Urban). Using these dictionaries 
you can *annotate* the original text and bring it to interactive life - for example hyperlinks to wikidata, or 
co-occurrence of terms in text. You can also use our tools to create indexes for chapters.

# the basic hackathon structure and goals

Because people are distributed over time and space we recoomand a basic activity/template which doesn't
require interactive coordination. We are used to Github tools for sharing discussion, and we've set out a self-paced 
plan based on converting a single Chapter (there are 50 to choose from!). 

## what you need
* enthusiasm. That's really the only requirement. Continued occasional activity over a week is very useful
* organization. It helps if material is well organized and can be discovered through links.
* experimental. We'll all be doing new things and often they won't work first time.
* collaboration. Very valuable.
* documentation. Clear outputs that help others. We are very keen to see languages other that EN, and links to Wikidata. Useful to know how to use a text editor rather than Word.

### valuable if you have them 
* HTML
* Python
* Wikidata
* Climate (science, politics, etc.)


## coordination
You may already have a real-life team and this should work well. Choose an interesting Chapter and post which and
who you are. (All activity is fully OpenNotebook Science). Record your progress on our Github (we'll give permissions) 

## template
* clone https://github.com/petermr/semanticClimate
* copy your chapter to .../semanticClimate/ipcc/ar6/wg3
* run script or notebook to:
  - add Chapter to CProject (corpus)
  - convert PDF to HTML
  - extract words
  - create chapter-dictionary
  - add Wikidata links if missing
  - annotate chapter
This will be the basic activity. Some may find it useful to work in teams. We'll coordinate people who are looking for 
partners/Chapters
  - 
If during the week we have N groups and they have each created a semantic Chapter, dictionaries and annotation
that will be a great uccess.

## extensions
There are a huge number of things that can be done with semantic material. We welcome hackers who want to explore this.


