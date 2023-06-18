# Projects for online collaborators/registrants (especially Wikimedia)


# IPCC/SYR statements for ingestion into Wikibase

The file https://github.com/petermr/semanticClimate/blob/main/ipcc/ar6/)/syr/lr/total_pages_groups_confidence.html contains several hundred paragraphs of the form:
```
2.1.1.bObserved increases in well-mixed GHG concentrations since around 1750 are unequivocally caused by GHG emissions from human activities. Land and ocean sinks have taken up a near-constant proportion (globally about 56% per year) of CO2 emissions from human activities over the past six decades, with regional differences *(high confidence*

). In 2019, atmospheric CO2 concentrations reached 410 parts per million (ppm), CH4 reached 1866 parts per billion (ppb) and nitrous oxide (N2O) reached 332 ppb11. Other major contributors to warming are tropospheric ozone (O3) and halogenated gases. Concentrations of CH4 and N2O have increased to levels unprecedented in at least 800,000 years *(very high confidence*

), and there is *high confidence*
that current CO2 concentrations are higher than at any time over at least the past two million years. 

Since 1750, increases in CO2 (47%) and CH4 (156%) concentrations far exceed – and increases in N2O (23%) are similar to – the natural multi-millennial changes between glacial and interglacial periods over at least the past 800,000 years (*very high confidence*`
```
These 4 snippets can be extracted into records in a Wikibase. Egon and Lars Willighagen have prototyped this https://kg-ipclimatec-reports.wikibase.cloud/wiki/Main_Page . There are about 1000 confidence statements. Can we get Wikimedia tools to allow quality edits to be uploaded rapidly?

# IPCC/SYR links to create a knowledge graph.

SYR/LR contains about 1000 links to other records, especially WGI/II/III SPM. We have extracted the SYR to WGI links in: `total_pages_groups_table.csv`
which contains a CSV file of the form
````
SYR_para_id SYR_text IPCC_Link WGI_para_id WGI_text
````
This is a link (edge) between 2 annotated nodes. Can we combine them into a kowledge graph and display with, e.g. neo4j, obsidian, etc. Can we analyse them with SPARQL?

