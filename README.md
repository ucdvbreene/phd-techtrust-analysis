PhD TechTrust Analysis

Overview
This repository contains the analysis for Technology Trust (TechTrust) in AI-assisted credit assessment. The study examines participant sentiment, trust calibration, and correlations between AI trust factors and participant responses.
Key analyses include:
Participant sentiment analysis before and after explanations
Calibration of trust relative to peers
Pearson and Spearman correlations between high-level themes and TechTrust scores
Multiple-testing corrected significance (Bonferroni, Holm, BH/FDR)
Visualizations: lollipop charts, scatter plots, and correlation heatmaps


Folder Structure
phd-techtrust-analysis/
│
├─ data/raw/           # Original Excel datasets
├─ notebooks/          # Jupyter notebooks for analysis
├─ results/            # Generated figures, tables, and output files
├─ docs/               # Methodology notes, supplementary materials
├─ .gitignore          # Files/folders ignored by Git
└─ README.md           # This file


Requirements
Python 3.x with the following libraries:
pip install pandas numpy scipy statsmodels matplotlib seaborn textblob
