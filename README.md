# Scraping India's Parliament Websites To Extract Questions and Answers

During every Parliament session (Lok Sabha or Rajya Sabha), the first hour is called the Question Hour and is dedicated for members of parliament to ask questions to the ministers and to hold the government accountable. The answers that the government provides through these questions become a crucial source of data and information for journalists.

In India, where official reports may be delayed or be unavailable online, Parliament Questions help journalists access latest data on a wide range of issues.

This automatic scraper daily extracts questions and answers from <b>both the Lok Sabha and Rajya Sabha</b> based on the ministry <b> and exports a csv to the repository with links to the answers</b>. It also sends you an email when new questions are uploaded.

The scraper, by default extracts answers given by the Women and Child Development Ministry but the code can be customised by just changing the name of the ministry.

## Notebooks

I have also uploaded a jupyter notebook named ```Parliament_Questions.ipynb``` in case you wish to manually do the scraping. Running the notebook will give you two csv files for Lok Sabha and Rajya Sabha data.

The notebook also has notes on all the ways to customise and edit the code to fit your need




