import numpy as np
import pandas as pd

def compute_technology_trust(participant_sentiment_df, factor_cols, weights):
    """
    Compute weighted TechTrust score per participant.
    """
    assert np.isclose(sum(weights), 1), "Weights must sum to 1"
    participant_sentiment_df['TechTrust'] = participant_sentiment_df[factor_cols].mul(weights).sum(axis=1)
    return participant_sentiment_df

def bootstrap_ci(participant_sentiment_df, n_boot=10000):
    """
    Bootstrap 95% confidence interval for TechTrust.
    """
    techtrust_values = participant_sentiment_df['TechTrust'].dropna().values
    boot_means = [np.mean(np.random.choice(techtrust_values, size=len(techtrust_values), replace=True)) 
                  for _ in range(n_boot)]
    boot_means = np.array(boot_means)
    ci_lower = np.percentile(boot_means, 2.5)
    ci_upper = np.percentile(boot_means, 97.5)
    boot_mean = np.mean(boot_means)
    return boot_mean, ci_lower, ci_upper

