import requests
import json
from twitter import *
import csv
import pandas as pd
from sentiments import world_sentiments, india_sentiments
from word_cloud import generate_clouds 

def main_func():
	consumer_key = 'XXXX'
	consumer_secret = 'XXXX'
	access_token = 'XXXX'
	access_secret = 'XXXX'

	t = Twitter(auth = OAuth(access_token, access_secret, consumer_key, consumer_secret))

	trends_india = t.trends.place(_id = 2282863)
	trends_world = t.trends.place(_id = 1)

	with open('trends_world.json', 'w', encoding = 'utf-8') as out1:
		json.dump(trends_world,out1, ensure_ascii = False, indent = 4)

	with open('trends_india.json', 'w', encoding = 'utf-8') as out2:
		json.dump(trends_india,out2, ensure_ascii = False, indent = 4)

	top_3_world = [trends_world[0].get('trends')[i].get('name') for i in range(3)]
	top_3_india = [trends_india[0].get('trends')[i].get('name') for i in range(3)]

	file_names_world = ['world_1.csv', 'world_2.csv', 'world_3.csv']
	file_names_india = ['india_1.csv', 'india_2.csv', 'india_3.csv']

	for i in range(len(top_3_world)):

		z=[]
		a = t.search.tweets(q = top_3_world[i], lang = 'en', encoding = 'utf-8', tweet_mode="extended", result_type = 'recent', count = 1000, entities = False)
		z = [tweet['full_text'] for tweet in a.get('statuses')]

		df = pd.DataFrame(z, columns=['world'])
		df.to_csv(file_names_world[i])

	for i in range(len(top_3_india)):
		
		z=[]
		a = t.search.tweets(q = top_3_india[i], lang = 'en', encoding = 'utf-8', tweet_mode="extended", result_type = 'recent', count = 1000, entities = False)
		z = [tweet['full_text'] for tweet in a.get('statuses')]

		df = pd.DataFrame(z, columns=['india'])
		df.to_csv(file_names_india[i])

	# world_dict = {}
	# india_dict = {}

	# for topic, sentiments in zip(top_3_world, world_sentiments()):
	# 	world_dict[topic] = sentiments

	# for topic, sentiments in zip(top_3_india, india_sentiments()):
	# 	india_dict[topic] = sentiments

	generate_clouds()

	return top_3_world, world_sentiments(), top_3_india, india_sentiments()