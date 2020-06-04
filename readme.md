# Team Assignment 2: Building a Text Mining Pipeline - Team 4
## A reproducible research workflow: JSON parsing and text mining in Python, R + RMarkdown

This is a workflow using GNU Make, Python and R for a reproducible research workflow, following the principles of [tilburgsciencehub.com](http://tilburgsciencehub.com/workflow). 

This respository consists of 2 parts:

1. Pipeline stage "data-preparation"
  - Download raw JSON data in a zip file
  - Unzip data
  - Parse JSON data to CSV file
  - Load CSV file, and enrich textual data with text mining metrics using Python's TextBlob package and Vader packge for sentiment analysis
2. Pipeline stage "analysis"
  - Load final output file from previous pipeline stage, run precleaning code
  - Produce RMarkdown HTML output with analysis report
  
## Dependencies
- Python via the Anaconda distribution
- TextBlob via `pip install -U textblob`
- Vader Sentiment via `pip install -U vaderSentiment`
- Langdetect via `pip install langdetect`
- NLTK dictionaries; open Python, then type
  ```
  import nltk
  nltk.download('punkt')
  ```
  
- Gnu Make
- R and the following packages:

```
install.packages(c("stargazer", "knitr", "data.table", "ggplot2",“wordcloud”,“tdm”)
require(devtools)
install_github("Displayr/flipTime")
```

Detailed installation instructions can be found here: [tilburgsciencehub.com/tutorial](http://tilburgsciencehub.com/tutorial)

## How to get started
The best way to get started is by following [the tutorial from our awesome lecturer](http://tilburgsciencehub.com/tutorial).

- Download this repository (either by forking and then cloning, or as a template)
- Open Terminal in project's main directory, type make
- The src/data-preparation and src/analysis directories contain the specific workflow for each stage of the pipeline.

