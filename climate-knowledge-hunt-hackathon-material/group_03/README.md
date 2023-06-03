## Group Lead
Shweata N. Hegde

## Group Participants
- Jayant Maini
- Vineeta Sharma
- Saksham
- Komal Rani
- Sushree Sumita

## What we did
The group explored the structure and contents of IPCC Reports. We also toured the [Wikibase Instance](https://kg-ipclimatec-reports.wikibase.cloud/). Later, we curated terms related to migration, created an AMI dictionary and used it to search some chapters of IPCC Report. 

### Hack session 01
We looked at the [PDF version of Synthesis Report](/ipcc/ar6/syr/lr/fulltext.pdf) to get a feel for what the how information is represented in these reports. We then explored the [HTML version](/ipcc/ar6/syr/lr/html/fulltext/groups_groups.html) of the report and brainstormed why HTML versions are better than dumb PDFs. 

We browsed through [Wikibase](https://kg-ipclimatec-reports.wikibase.cloud/), looked at [Items](https://kg-ipclimatec-reports.wikibase.cloud/) and ran [SPARQL Queries](https://kg-ipclimatec-reports.wikibase.cloud/query/#PREFIX%20wdt%3A%20%3Chttps%3A%2F%2Fkg-ipclimatec-reports.wikibase.cloud%2Fprop%2Fdirect%2F%3E%0APREFIX%20wd%3A%20%20%3Chttps%3A%2F%2Fkg-ipclimatec-reports.wikibase.cloud%2Fentity%2F%3E%0A%0ASELECT%20%3Fsection%20%3FsectionLabel%20%3FcitedSection%20%3FcitedSectionLabel%20WHERE%20%7B%0A%20%20%3Fsection%20wdt%3AP1%20wd%3AQ18%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20wdt%3AP11%20%3FcitedSection%20.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D)

### Hack Session 02
In the second session, Jayant made a list of migration related terms. SNH re-purposed old code to convert this list into an AMI dictionary. SNH ran [`docanalysis`](https://github.com/petermr/docanalysis/wiki/docanalysis-Tutorial#installing-docanalysis) locally to pull out sentences that mentioned the terms from the newly created dictionary. 

```
docanalysis --project_name D:\climate-knowedge-hunt-20230519\ipcc --search_html --dictionary D:\climate-knowedge-hunt-20230519\migration.xml --output migration_syr.csv
```

- Migration dictionary: https://github.com/semanticClimate/climate-knowedge-hunt-20230519/blob/main/migration.xml

- Sentences with migration-related terms pulled out from Synthesis Report: https://github.com/semanticClimate/climate-knowedge-hunt-20230519/blob/main/ipcc/migration_syr.csv

Most of the group members managed to run the script to create dictionary. SNH demonstrated how Git, the Version Controlling software, works. We briefly looked at the sentences pulled from the synthesis report to check whether they had relevant information related to migration. 

### Final Presentation
We presented our work to the larger group at the end of the hack day. 
- [Presentation](/climate-knowledge-hunt-hackathon-material/group_03/group_3_final_presenation_climate_knowledge_hunt.pptx) (Credits: Jayant Maini and Vineeta Sharma)
### Problems
Google Colab has upgraded its Python to `3.10`. But `docanalysis` is only compatible with Python Version 3.8 and below. Group participants tried to install Python and run `docanalysis` locally, but we ran out of time. 
