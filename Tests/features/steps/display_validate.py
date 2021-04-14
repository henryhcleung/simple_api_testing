from behave import *
from behave_pandas import table_to_dataframe, dataframe_to_table
import socket
import requests
import http.client, urllib.parse
import ssl
import logging
import json

#logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('response.log', 'w', 'utf-8'), ])

# Class for row values
class rowValues:
    postId = ""
    fid = ""
    name = ""
    email = ""
    body = ""

# Convert table data
def transformToTable(rawData):
    logging.info("table is loading")
    table = []
    for i in range(1, rawData.RowCount):
        row = rowValues()
        row.postId = rawData.Value[i, 0]
        row.fid = rawData.Value[i, 1]
        row.name = rawData.Value[i, 2]
        row.email = rawData.Value[i, 3]
        row.body = rawData.Value[i, 4]
        table.append(row)
    return table

@given('the api is ok')
def step_get_api(context):
    pass

@when('send a get request "{url}"')
def step_request_get(context, url):
    logging.info(url)
    response = requests.get(url)
    context.response_code = response.status_code
    context.body = response.text
    response.close()

@then('return a "{code}" response code')
def check_request_code(context, code):
    logging.info(context.response_code)
    assert context.response_code == int(code)

@then('return correct information')
def step_load_table(context):
    for row in context.table:
       postId = row['postId']
       fid = row['fid']
       name = row['name']
       email = row['email']
       body = row['body']

       context.postId = postId
       context.fid = fid
       context.name = name
       context.email = email
       context.body = body

       
def check_validate_result(context, postID, fid, name, email, body):
    logging.info(context.body)
    data = json.loads(context.body)
    print(context.body)

    assert data[0]['postId'] != ""
    assert data[0]['id'] != ""
    assert data[0]['name'] != ""
    assert data[0]['email'] != ""
    assert data[0]['body'] != ""
    x = 5
    for i in range (x):
        for x in data:
            assert data[i]['postId'] == postID
            assert data[i]['postId'] == fid
            assert data[i]['postId'] == name
            assert data[i]['postId'] == email
            assert data[i]['postId'] == body
