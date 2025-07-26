#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('iris.csv')
    summary = df.describe()
    print('Summary statistics:')
    print(summary)
    # Plot sepal length distribution
    plt.hist(df['sepal_length'], bins=10, color='#00A8A8')
    plt.title('Sepal Length Distribution')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Frequency')
    plt.savefig('sepal_length_hist.png')

if __name__ == '__main__':
    main()
