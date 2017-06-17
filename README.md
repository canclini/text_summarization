## About
As part of the Text Analysis Module from the [CAS Machine Intelligence](https://weiterbildung.zhaw.ch/de/school-of-engineering/programm/cas-machine-intelligence.html) at [ZHAW](https://www.zhaw.ch), I wrote a paper in german to get familiar with the Topi Text Summarization.

## Dependencies
* pandoc
* TeX distribution (only for PDF)
* bibtex file (generated with Zotero)
* Sublime Text 3 (ST3)
  * Markdown Extended
  * CiteBibtex
  * Pandoc

## Hints
in SublimeText 3:
* `F10` shows the entries from the bibtex.bib
* "CiteBibtex: extract citations in current file" -> extracts the used citations and stores them in a local bibex file
* "Pandoc" -> "PDF" creates the PDF file from the markdown file

on the command line run the following command to create the PDF document from the markdown file:
```
pandoc TextSummarization.mdown --latex-engine=xelatex --filter pandoc-citeproc -o Text\ Summarization\ \(Marcel_Canclini\).pdf
```
