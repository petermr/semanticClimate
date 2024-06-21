## Note
Experimental

### more exptl
another line

## Goal 


Proof-of-concept of transforming the IPCC reports from PDFs into navigable hypermedia formats to better facilitate understanding and discourse by various stakeholders

## Approach

The general approach is to extract/annotate key discourse elements from the IPCC report into a set of granular markdown files, organized according to a (modified) [discourse graph data model](https://network-goods.notion.site/The-Discourse-Graph-starter-pack-312374c813b24ec6b4d53a054371ee5a). 

For example, to start with, we explore unpacking executive summaries (which contain [[conclusions]]) into their substantiating [[claims]], which are then linked to substantiating [[evidence]], both discussed in the rest of the report after the executive summary.

These can then be used as a substrate to build more navigable and explorable (via hypermedia) interfaces for understanding the key claims and recommendations of the report.

Start [[index.md]]

Current state example:
![[example-IPCC-discourse-graph.png]]
