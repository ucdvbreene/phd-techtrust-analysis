import pandas as pd
import numpy as np
from scipy.stats import shapiro, anderson, pearsonr, spearmanr

def run_normality_tests(df, factor_cols):
    """Run Shapiro-Wilk and Anderson-Darling tests on factor columns."""
    normality_results = []

    for col in factor_cols:
        data = df[col].dropna()
        if len(data) < 3:
            normality_results.append([col, np.nan, np.nan, "Too few values", np.nan, "Too few values"])
            continue

        # Shapiro-Wilk
        sw_stat, sw_p = shapiro(data)
        sw_interp = "Normal" if sw_p > 0.05 else "Not normal"

        # Anderson-Darling
        ad_result = anderson(data)
        ad_stat = ad_result.statistic
        critical_5pct = ad_result.critical_values[2]  # 5% level
        ad_interp = "Normal" if ad_stat < critical_5pct else "Not normal"

        normality_results.append([col, sw_stat, sw_p, sw_interp, ad_stat, ad_interp])

    normality_df = pd.DataFrame(
        normality_results,
        columns=["Factor", "SW W", "SW p", "Shapiro Interpretation",
                 "AD Statistic", "AD Interpretation"]
    )
    return normality_df

def run_correlation_tests(df, factor_cols):
    """Compute Pearson and Spearman correlations and p-values between factor columns."""
    factor_data = df[factor_cols].astype(float)

    pearson_results = pd.DataFrame(index=factor_cols, columns=factor_cols)
    pearson_pvals = pd.DataFrame(index=factor_cols, columns=factor_cols)
    spearman_results = pd.DataFrame(index=factor_cols, columns=factor_cols)
    spearman_pvals = pd.DataFrame(index=factor_cols, columns=factor_cols)

    for i, f1 in enumerate(factor_cols):
        for j, f2 in enumerate(factor_cols):
            x = factor_data[f1].dropna()
            y = factor_data[f2].dropna()
            common_idx = x.index.intersection(y.index)
            x = x.loc[common_idx]
            y = y.loc[common_idx]

            if len(x) > 1:
                # Pearson
                r, p = pearsonr(x, y)
                pearson_results.loc[f1, f2] = r
                pearson_pvals.loc[f1, f2] = p
                # Spearman

