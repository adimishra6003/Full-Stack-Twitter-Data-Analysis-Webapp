import pandas as pd
from PIL import Image
import numpy as np
from wordcloud import WordCloud

def generate_clouds():

	df_india = pd.read_json('trends_india.json', encoding = 'utf-8')
	df_world = pd.read_json('trends_world.json', encoding = 'utf-8')

	top_india_trending = [df_india.trends[0][i].get('name') for i in range(len(df_india.trends[0]))]
	top_world_trending = [df_world.trends[0][i].get('name') for i in range(len(df_world.trends[0]))]

	india = ' '.join(top_india_trending)
	india = india.replace('_', '')

	world = ' '.join(top_world_trending)

	char_mask = np.array(Image.open("twitter_mask.png"))
	wc1 = WordCloud(width = 800, height = 400,max_font_size=100, contour_color='red', include_numbers=True, min_font_size=1, mode='RGBA', background_color=None, colormap='prism', mask=char_mask, font_path='font/arial-unicode-ms.ttf').generate(india)
	wc1.to_file('static/india_cloud.png')

	wc2 = WordCloud(width = 800, height = 400, contour_color='red', include_numbers=True, min_font_size=1, mode='RGBA', background_color=None, colormap='prism', mask=char_mask, font_path='font/arial-unicode-ms.ttf').generate(world)
	wc2.to_file('static/world_cloud.png')