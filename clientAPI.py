# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""{
  "username": "91819ede-4166-4871-bdb4-c58ee8e44e2c-bluemix",
  "password": "77f3fee25e14cd0c13c8ec0cf6d9b8aa364ef63c53dd5d3c257570916855a553",
  "host": "91819ede-4166-4871-bdb4-c58ee8e44e2c-bluemix.cloudant.com",
  "port": 443,
  "url": "https://91819ede-4166-4871-bdb4-c58ee8e44e2c-bluemix:77f3fee25e14cd0c13c8ec0cf6d9b8aa364ef63c53dd5d3c257570916855a553@91819ede-4166-4871-bdb4-c58ee8e44e2c-bluemix.cloudant.com"
}"""
import os
import requests
from flask import Flask, jsonify
import couchdb
    
app = Flask(__name__)

@app.route('/dbquery/<query>')
def query_db(query):
    #vcap = json.loads(os.getenv("VCAP_SERVICES"))['cloudantNoSQLDB']

    
    cl_username = '91819ede-4166-4871-bdb4-c58ee8e44e2c-bluemix'
    cl_password = "77f3fee25e14cd0c13c8ec0cf6d9b8aa364ef63c53dd5d3c257570916855a553"

    url         = "https://91819ede-4166-4871-bdb4-c58ee8e44e2c-bluemix.cloudant.com"
    auth        = ( cl_username, cl_password )

    auth        = ( cl_username, cl_password )

    couch = couchdb.Server("https://91819ede-4166-4871-bdb4-c58ee8e44e2c-bluemix.cloudant.com")
    couch.resource.credentials = (cl_username, cl_password)
    db = couch['friend_db']
    for doc in db:
        return str(doc) 
    r = requests.post( url + '/_all_docs', auth=auth )
    return r.text


        

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/api/register')
def Register():
    message = {
        'success': False,
        'message': 'unimplemented'
    }
    return jsonify(results=message)

@app.route('/api/register')
def Login():
    message = {
        'success': False,
        'message': 'unimplemented',
        'token': 'dfsdjfdsfw4q4'
    }
    return jsonify(results=message)

@app.route('/api/myprofile')
def MyProfile():
    profiledata = {
        'success': False,
        'message': 'unimplemented'
    }
    return jsonify(results=profiledata)


@app.route('/api/editprofile')
def EditProfile():
    editmessage = {
        'success': False,
        'message': 'unimplemented'
    }
    return jsonify(results=editmessage)

@app.route('/api/register')
def Search():
    searchresults = {
        'success': False,
        'message': 'unimplemented',
        'list': [
            {'name': 'John', 'age': 28},
            {'name': 'Bill', 'val': 26}
        ]
    }
    return jsonify(results=searchresults)

@app.route('/api/viewprofile/<id>')
def ViewProfile():
    profiledata = {
        'success': False,
        'message': 'unimplemented'
    }
    return jsonify(results=profiledata)

@app.route('/api/getfriends')
def GetFriends():
    friendlist = {
        'success': False,
        'message': 'unimplemented'
    }
    return jsonify(results=friendlist)

@app.route('/api/resquestfriend/<id>')
def RequestFriend():
    friendrequest = {
        'success': False,
        'message': 'unimplemented'
    }
    return jsonify(results=friendrequest)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
