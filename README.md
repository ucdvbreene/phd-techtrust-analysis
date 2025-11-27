# PhD TechTrust Analysis


Overview
This repository contains the analysis for Technology Trust (TechTrust) in AI-assisted credit assessment. The study examines participant sentiment, trust calibration, and correlations between AI trust factors and participant responses.
Key analyses include:
Participant sentiment analysis before and after explanations
Calibration of trust relative to peers
Pearson and Spearman correlations between high-level themes and TechTrust scores
Multiple-testing corrected significance (Bonferroni, Holm, BH/FDR)
Visualizations: lollipop charts, scatter plots, and correlation heatmaps

# PhD TechTrust Analysis

It includes a Python package `techtrust_core` for:
- Computing sentiment from participant quotes  
- Calculating weighted Technology Trust scores  
- Generating basic visualizations  

It includes a Python package `techtrust_stats` for:
- Normal Distribtuion Checks  
- Pearson and Spearman Correlation and P_Values  
- Multiple Comparision Control


### 1. Clone the repository
```bash
git clone https://github.com/ucdvbreene/phd-techtrust-analysis.git
cd phd-techtrust-analysis

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

>>>>>>> e58eeac (Add techtrust_core and techtrust_stats packages with notebooks and dummy data)
