import os
import urllib.parse
import requests
import argparse


from dotenv import load_dotenv


parse = argparse.ArgumentParser(
    description='Описание что делает программа'
)
parse.add_argument('link', help='ссылка')
args = parse.parse_args()
user_url = args.link

load_dotenv()
token = os.getenv["BITLY_TOKEN"] 

def is_bitlink(bitlink, token):
    headers = {"Authorization": f'Bearer {token}'}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(url, headers=headers)
    return response.ok
    

def shorten_link(new_user_url, token):
    headers = {"Authorization": f'Bearer {token}'}
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {"long_url": new_user_url}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink

def count_clicks(token, bitlink):
    count_clicks_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'units': -1}
    response = requests.get(count_clicks_url, headers=headers, params=payload)
    response.raise_for_status()
    click_score = response.json()['total_clicks']
    return click_score

if __name__ == "__main__":
    parsed_user_url = urllib.parse.urlparse(user_url)
    bitlink = parsed_user_url.netloc + parsed_user_url.path

# https://bit.ly/3H9UC7R
# link = 'https://www.google.com/search?q=rjn&oq=rjn&aqs=chrome.0.69i59j69i57j69i60l2j69i65.3247j0j7&sourceid=chrome&ie=UTF-8'
    if not parsed_user_url.scheme:
        new_user_url = f'http://{user_url}' 
    else:
        new_user_url = user_url
      
    try:
        if is_bitlink(bitlink, token):
            click_score = count_clicks(token, bitlink)
            print('Кликов по ссылке: ', click_score)
        else:
            print('Битлинк: ',         shorten_link(new_user_url, token))
    except requests.exceptions.HTTPError:
        print('неправильная ссылка')
