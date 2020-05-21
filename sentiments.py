import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns


file_names_world = ['world_1', 'world_2', 'world_3']
file_names_india = ['india_1', 'india_2', 'india_3']


def world_sentiments():
    top_sentiments=[]
    for i in file_names_world:
        df = pd.read_csv(i+'.csv')
        df.columns = [0, 1]

        for j in range(df.shape[0]):
            df[1][j] = df[1][j].split("http")[0]
            try:
                df[1][j] = df[1][j].split(":")[1]
            except:
                pass

        sia = SentimentIntensityAnalyzer()
        df['sentiment'] = [sia.polarity_scores(tweet)['compound'] for tweet in list(df[1])]
        plt.figure(figsize = (10, 4))
        sns.set(style='darkgrid')
        dist = sns.distplot(df.sentiment, color = 'red', axlabel = 'Sentiment')
        plt.title('Trending #'+i)
        plt.ylabel('Probability Density')
        plt.savefig('static/'+i+'.jpg')
        top_sentiments.append(df.sentiment.mean())
    return top_sentiments

def india_sentiments():
    top_sentiments=[]
    for i in file_names_india:
        df = pd.read_csv(i+'.csv')
        df.columns = [0, 1]

        for j in range(df.shape[0]):
            df[1][j] = df[1][j].split("http")[0]
            try:
                df[1][j] = df[1][j].split(":")[1]
            except:
                pass

        sia = SentimentIntensityAnalyzer()
        df['sentiment'] = [sia.polarity_scores(tweet)['compound'] for tweet in list(df[1])]
        plt.figure(figsize = (10, 4))
        sns.set(style='darkgrid')
        dist = sns.distplot(df.sentiment, color = 'red', axlabel = 'Sentiment')
        plt.title('Trending #'+i)
        plt.ylabel('Probability Density')
        plt.savefig('static/'+i+'.jpg')
        top_sentiments.append(df.sentiment.mean())
    return top_sentiments