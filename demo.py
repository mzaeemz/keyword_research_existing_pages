# Author: Skyler Reeves | Ardent Growth | July 2020

location = "Louisville, KY" #@param {type:"string"}
engine = "google" #@param ["google", "google scholar", "bing", "baidu", "yandex", "yahoo", "ebay"]
url = #Insert URL String Here from Github 

from serpapi.google_search_results import GoogleSearchResults
import pandas as pd
import csv

#Add your SERP API KEY between the '' below
api_key = 'API_KEY_GOES_HERE'

df1 = pd.read_csv(url) # Dataset is now stored in a Pandas Dataframe

# The While Loop putting items into a queue
query_queue = []
i = 0
while i < data_frame_size:
 query = df1.iloc[i][0]
 query_queue.append(query)
 i+=1

for search_query in query_queue:
 query_params = {
 "location": location,
 "engine": engine,
 "api_key": api_key,
 "q": search_query
 }
 search_client = GoogleSearchResults(query_params)
 search_results = search_client.get_dict()
 for link in search_results['organic_results']:
   print(link['link'])
