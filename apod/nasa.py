#!/usr/bin/env python
#-*-coding:utf-8-*-

import os
from dotenv import load_dotenv
import json
import requests

def picture_of_the_day():
    nasaapikey = os.getenv('NASAAPIKEY')
    host = 'https://api.nasa.gov/planetary/apod'
    r = requests.get(host, params={'api_key': nasaapikey})

    if r.status_code != 200:
        raise requests.exceptions.HTTPError(r.reason)
    else:
        limit = r.headers['X-RateLimit-Limit']
        limit_remaining = r.headers['X-RateLimit-Remaining']
        print('Remaining: ', limit_remaining)
        print('Limit: ', limit)
        apodjsonobj = r.json()
        apodjson = json.dumps(apodjsonobj, sort_keys=True, indent=4)
        return apodjson

def main():
    load_dotenv()
    print('NASA APOD')
    apoddata = picture_of_the_day()
    print(apoddata)

if __name__ == "__main__":
    main()
