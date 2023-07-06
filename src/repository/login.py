from __future__ import print_function
import json

import os.path
from pathlib import Path
from httplib2 import Http
from fastapi.responses import RedirectResponse
import requests


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from urllib.parse import urlencode, quote_plus



# If modifying these scopes, delete the file token.json.
def google_login():
    token_request_uri = "https://accounts.google.com/o/oauth2/auth"
    response_type = "code"
    client_id = "51231847720-s25mhf3poa81tl5dfqpbfsuad8dhp8uf.apps.googleusercontent.com"
    redirect_uri = "http://127.0.0.1:8000"
    scope = "https://www.googleapis.com/auth/userinfo.profile"
    url = f"{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
    
    return print(url)


def google_authenticate(code):
    parser = Http()
    login_failed_url = '/'
    # if 'error' in request.GET or 'code' not in request.GET:
    #     return RedirectResponse('{loginfailed}'.format(loginfailed = login_failed_url))

    access_token_uri = 'https://accounts.google.com/o/oauth2/token'
    redirect_uri = "http://127.0.0.1:8000"
    payload = {
        'code': code,
        'redirect_uri':redirect_uri,
        'client_id': '51231847720-s25mhf3poa81tl5dfqpbfsuad8dhp8uf.apps.googleusercontent.com',
        'client_secret': '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',
        'grant_type':'authorization_code'
    }
    params = urlencode(payload, quote_via=quote_plus)
    headers={'content-type':'application/x-www-form-urlencoded'}
    resp, content = parser.request(access_token_uri, method = 'POST', body = params, headers = headers)
    token_data = json.loads(content)
    print(f"{token_data=}")
    resp, content = parser.request("https://www.googleapis.com/oauth2/v1/userinfo?access_token={accessToken}".format(accessToken=token_data['access_token']))
    #this gets the google profile!!
    google_profile = json.loads(content)
    print(google_profile)
    #log the user in-->
    #HERE YOU LOG THE USER IN, OR ANYTHING ELSE YOU WANT
    #THEN REDIRECT TO PROTECTED PAGE
    # return RedirectResponse('/')

