import requests
from random import randrange
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "security.loc",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.97 Safari/537.36",
}

siteUrl = 'http://security.loc/getHeader.php'
response = requests.get(siteUrl, headers=headers)
urlText = response.text
soup = BeautifulSoup(urlText, 'html.parser')


def __setInputValue(name):
    data = {
        "emails": {'mail', 'email'},
        "links": {'link', 'url', 'site', 'web', 'www'},
        "numbers": {'number', 'phone', 'call', 'mobile'},
        "others": {'year', 'month', 'day', 'age', 'zip'},
    }
    X = 0
    for email in data["emails"]:
        if name.lower() in email and X == 0:
            X = 1
            return 'john1@gmail.com'
    for link in data["links"]:
        if name.lower() in link and X == 0:
            X = 1
            return 'https://www.site.com/'
    for number in data["numbers"]:
        if name.lower() in number and X == 0:
            X = 1
            return '5558251545'
    for other in data["others"]:
        if name.lower() in other and X == 0:
            X = 1
            return randrange(10, 12)
    return 'JohnDroma'


def __createUrlAction(url):
    if 'http' in url:
        return url
    else:
        parsed_uri = urlparse(siteUrl)
        if url.startswith('/'):
            getHost = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        else:
            getHost = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        result = getHost + url
        return result


actions = soup.find_all('form')
if len(actions) > 0:

    for action in actions:

        count = 0
        if action.get('action') is not None and action.get('method') is not None:
            formUrl = __createUrlAction(action.get('action'))
            formMethod = action.get('method').lower()
            allInputNames = {}
            # ++++
            count = count + 1
            inputs = action.find_all('input')
            textareas = action.find_all('textarea')

            for input in inputs:
                inputName = input.get('name')
                if input.get('type') != 'submit' and input.get('type') != 'hidden' and inputName is not None:
                    inputName = input.get('name')
                    allInputNames.update({inputName: __setInputValue(inputName)})
            for textarea in textareas:
                textareaName = textarea.get('name')
                allInputNames.update({textareaName: __setInputValue(textareaName)})
            #dictKey = allInputNames.keys()
            #print(allInputNames[1]())
            print(formUrl)
            print(formMethod)
            print(allInputNames)
            if formMethod == 'post':
                postResponse = requests.post(formUrl, allInputNames)
                #print(postResponse.text)
            # else:
            #     getResponse = requests.get(formUrl, allInputNames)
            #     print(getResponse.text)



# if os.path.isfile('urls.txt'):
#     with open('urls.txt') as file:
#         array = file.readlines()
#         for url in array:
#             r = requests.get(url)
#             print(r.text)
# else:
#     open('urls.txt', 'a')
