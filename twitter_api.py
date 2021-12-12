import requests
import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_ROUTE = 'https://api.twitter.com/2/tweets/search/recent'
DEFAULT_MAX_RESULTS = 100

def get_tweets(query, exact=True, next_token_page=None ,max_results=DEFAULT_MAX_RESULTS):
    if exact:
        query_str = '"{}" lang:pt'
    else:
        query_str = '{} lang:pt'
    params = {
        'query': query_str.format(query),
        'max_results': max_results,
    }

    headers = {
        'authorization': 'Bearer {}'.format(os.getenv('TWITTER_TOKEN')),
    }

    if next_token_page:
        params['next_token'] = next_token_page

    response = requests.get(DEFAULT_ROUTE, params=params, headers=headers)
    return response.json()