# making or editing a chapter

Each WG contains about 20 Chapters as PDF, labelled `Chapter[0-9][0-9].pdf`; e.g. `Chapter07.pdf`.
We carry out the following steps:
* make a `CProject` (CorpusProject) containing each Chapter as a `CTree` (CorpusTree) in (make project)
* copy or rename the PDF to `<CTree>/fulltext.pdf`, e.g. `Chapter07/fulltext.pdf (make project)
* convert (all) `<CTree>/fulltext.pdf` to `<CTree>/fulltext.html`  (html option)

# make project and fulltext.pdf
Assume PDF(s) have been downloaded.
* Task: convert some or all of the PDFs  to `CTree` structure containing `fulltext.pdf`
* Uses: subset of `py4ami PROJECT` 
* Input: `*.pdf` in `<CProject>` directory
* Options: `filter input files by regex`
* Outputs:
  - `<CProject>/fulltext.pdf`
* Command: 
```buildoutcfg
py4ami PROJECT --project <project dir> --files <files 
    --keep <keep original PDFs>  --replace <yes/no for original files>
```
* Examples:
  - convert all PDF files (the default) in `wg3` to `fulltext.pdf`
  ```buildoutcfg
py4ami PROJECT --project /users/pm286/semanticClimate/ipcc/ar6/wg3
```
  - convert a single Chapter to `fulltext.pdf`
  ```
py4ami PROJECT --project /users/pm286/semanticClimate/ipcc/ar6/wg3 --files Chapter02.pdf
```
  - convert a list of Chapters (default extension pdf) to fulltext.pdf
```
py4ami PROJECT --project /users/pm286/semanticClimate/ipcc/ar6/wg3 --files Chapter02 Chapter14
``
  
# convert fulltext.pdf to HTML

Assume `CProject` with `fulltext.pdf` 
* Task: convert some or all of the PDFs to HTML. 
* Uses: subset of `py4ami PDF` 
* Input: `fulltext.pdf` in `<CTree>` directories
* Options: make raw HTML (page-formatted) and `*.flow.html` which can flow
* Outputs:
  - `<CProject>/fulltext.flow.html`
  - `<CProject>/fulltext.html`
* Command: 
```buildoutcfg
py4ami PDF --PROJECT <project dir> 
```
* Example:
```buildoutcfg
py4ami PDF --project /users/pm286/semanticClimate/ipcc/ar6/wg3
```
