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
Quick Start
Clone the repository:
git clone https://github.com/<your-username>/phd-techtrust-analysis.git
cd phd-techtrust-analysis
Run Jupyter notebooks:
jupyter notebook
Open the notebooks in the notebooks/ folder in order:
1. TAWE_Trust_Score.ipynb – Compute sentiment and calibrated trust scores
2. TAWE_TopicModelling_Checks.ipynb – Topic modelling & theme aggregation
3. Attitudes_towards_AI_Analysis.ipynb – Correlation analysis, normality checks, visualizations
Save results: Processed tables, plots, and figures are saved to results/.
Git Workflow
Check repository status
git status
Stage changes
git add .
Commit changes
git commit -m "Describe your changes here"
Push to remote
git push origin main
Note: If your Git identity is not set, configure it first:
git config --global user.name "Your Name"
git config --global user.email you@example.com
Notes
Correlations include multiple-testing corrections: Bonferroni, Holm, and BH/FDR.
Normality is checked using Shapiro–Wilk test.
Sample size is small (≈10 participants), so non-parametric tests (Spearman) are preferred.
