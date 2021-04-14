from behave import *
import socket
import requests
import http.client, urllib.parse
import ssl
import logging

#logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('response.log', 'w', 'utf-8'), ])

@given('the API is ready')
def step_given_api_is_ready(context):
    pass

@when('send a get request to tandem api "{url}"')
def step_send_get_request(context, url):
    response = requests.get(url)
    context.response_code = response.status_code

@then('we will received a "{code}" response code')
def step_validate_response(context, code):
    logging.info(context.response_code)
    assert context.response_code == int(code)