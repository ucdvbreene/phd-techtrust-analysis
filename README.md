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

This repository contains tools and notebooks for computing Technology Trust scores and performing related analyses.

It includes a Python package `techtrust_core` for:

- Computing sentiment from participant quotes  
- Calculating weighted Technology Trust scores  
- Generating basic visualizations  

## Quick Start

1. Clone this repository:
```bash
git clone https://github.com/ucdvbreene/phd-techtrust-analysis.git

from techtrust_core import compute_sentiment, compute_technology_trust

Requirements
Python 3.x with the following libraries:
pip install pandas numpy scipy statsmodels matplotlib seaborn textblob
=======
[![Python Version](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## Overview
This repository contains the analysis for **Technology Trust (TechTrust)** in AI-assisted credit assessment.  

The study examines:

- Participant sentiment **before and after explanations**
- Calibration of trust **relative to peers**
- **Pearson and Spearman correlations** between high-level themes and TechTrust scores
- **Multiple-testing corrections** (Bonferroni, Holm, BH/FDR)
- Visualizations including lollipop charts, scatter plots, and correlation heatmaps

---

## Installation

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
