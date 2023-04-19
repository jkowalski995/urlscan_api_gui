import requests
import json
import time


def api_call(url=None):
    """
    Will connect with urlscan.io API and retrieve an image (bytes) of provided url.
    :param url: (string) a string url of scanned website with or without https://www.
    :return: (bytes) image view in bytes object
    """
    with open('config.txt', 'r') as config:
        api_key = config.readline()[:-1]

    headers = {'API-Key': api_key, 'Content-Type': 'application/json'}
    data = {"url": url, "visibility": "private"}
    response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))
    print(response)
    uuid = response.json()['uuid']

    time.sleep(15)

    response = requests.get('https://urlscan.io/screenshots/' + uuid + '.png', headers=headers, data=json.dumps(data))
    print(response)
    img_bytes = response.content

    return img_bytes
