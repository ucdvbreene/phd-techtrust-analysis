import matplotlib.pyplot as plt
import numpy as np

def plot_participant_sentiment(participant_sentiment_df, features):
    mean_values = participant_sentiment_df[features].mean()
    std_values = participant_sentiment_df[features].std()
    x = np.arange(1, len(features)+1)

    plt.figure(figsize=(8,5))
    plt.plot(x, mean_values.values, marker='o', linestyle='-', color='royalblue', label='Mean')
    plt.fill_between(x, mean_values - std_values, mean_values + std_values, color='royalblue', alpha=0.2, label='±1 SD')
    plt.xticks(x, features, rotation=45)
    plt.title("TAWE Factor - Mean Sentiment")
    plt.xlabel("Features")
    plt.ylabel("Mean Sentiment / TechTrust")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_factor_distribution(one_hot_counts):
    features = one_hot_counts.index
    counts = one_hot_counts.values
    x = np.arange(1, len(features)+1)

    plt.figure(figsize=(8,5))
    plt.plot(x, counts, marker='o', linestyle='-', color='royalblue', label='Number of Quotes')
    plt.fill_between(x, counts, color='royalblue', alpha=0.2)
    plt.xticks(x, features, rotation=45)
    plt.title("TAWE Factor Total Responses")
    plt.xlabel("Features")
    plt.ylabel("Number of Quotes")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

