#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013-2014 Abram Hindle
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#Information and much of the code responsible for implementing the observer pattern with web sockets and clients and was taken from the CMPUT404 class notes

#In particular https://github.com/uofa-cmput404/cmput404-slides/tree/master/examples/ObserverExampleAJAX

#Copyright 2013 Abram Hindle

#Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

 #   http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


import flask
from flask import Flask, request
from flask_sockets import Sockets
import gevent
from gevent import queue
import time
import json
import os

app = Flask(__name__)
sockets = Sockets(app)
app.debug = True

def send_all(msg):
    #whenever we get a message from a socket add it to all listeners (which are queues)
    for client in myWorld.listeners:
        client.put(msg)

def send_all_json(obj):
    send_all(json.dumps(obj))

#class for our listeners
class Client:
    def __init__(self):
        #each listener is a queue
        self.queue = queue.Queue()

    def put(self, v):
        self.queue.put_nowait(v)

    def get(self):
        return self.queue.get()

class World:
    def __init__(self):
        self.clear()
        # we've got listeners now!
        self.listeners = list()
        
    def add_set_listener(self, listener):
        self.listeners.append( listener )

    def update(self, entity, key, value):
        entry = self.space.get(entity,dict())
        entry[key] = value
        self.space[entity] = entry
        self.update_listeners( entity )

    def set(self, entity, data):
        self.space[entity] = data

    def update_listeners(self, entity):
        '''update the set listeners'''
        for listener in self.listeners:
            listener(entity, self.get(entity))

    def clear(self):
        self.space = dict()

    def get(self, entity):
        return self.space.get(entity,dict())
    
    def world(self):
        return self.space

myWorld = World()        

def set_listener( entity, data ):
    ''' do something with the update ! '''

#myWorld.add_set_listener( set_listener )
        
@app.route('/')
def hello():
    '''Return something coherent here.. perhaps redirect to /static/index.html '''
    #https://www.w3schools.com/python/python_try_except.asp
    try:
        #https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask
        return flask.redirect("/static/index.html") #redirect to /static/index.html
    except:
        #https://stackoverflow.com/questions/7824101/return-http-status-code-201-in-flask
        #https://stackoverflow.com/questions/12435297/how-do-i-jsonify-a-list-in-flask
        return json.dumps("Error Redirecting"), 500 #500 not 400 because a redirection error would be on the server side

def read_ws(ws,client):
    '''A greenlet function that reads from the websocket and updates the world'''
    # XXX: TODO IMPLEMENT ME
    try:
        while True:
            #the message we get from the websocket
            msg = ws.receive()
            print("WS RECV: %s" % msg)
            if (msg is not None):
                packet = json.loads(msg)
                #for information on how to get key and value from python dictionary https://www.w3schools.com/python/python_dictionaries_access.asp
                for key in packet.keys():
                    #set our world with the entity and value we just received from the web socket
                    myWorld.set(key,packet[key])
                send_all_json( packet )
            else:
                break
    except:
        '''Done'''

@sockets.route('/subscribe')
def subscribe_socket(ws):
    '''Fufill the websocket URL of /subscribe, every update notify the
       websocket and read updates from the websocket '''
    # XXX: TODO IMPLEMENT ME
    client = Client()
    myWorld.add_set_listener(client) #create a new listener for our new socket
    g = gevent.spawn( read_ws, ws, client ) #spawn a thread to read from the web socket
    try:
        while True:
            # block here
            msg = client.get() #once there is data in the queue get it and send it through the socket
            ws.send(msg)
    except Exception as e:# WebSocketError as e:
        print("WS Error %s" % e)
    finally:
        clients.remove(client)
        gevent.kill(g)


# I give this to you, this is how you get the raw body/data portion of a post in flask
# this should come with flask but whatever, it's not my project.
def flask_post_json():
    '''Ah the joys of frameworks! They do so much work for you
       that they get in the way of sane operation!'''
    if (request.json != None):
        return request.json
    elif (request.data != None and request.data.decode("utf8") != u''):
        return json.loads(request.data.decode("utf8"))
    else:
        return json.loads(request.form.keys()[0])

@app.route("/entity/<entity>", methods=['POST','PUT'])
def update(entity):
    '''update the entities via this interface'''
    #https://www.w3schools.com/python/python_try_except.asp
    try:
        data = flask_post_json() #get the body using the given flask method
        myWorld.set(entity,data) #use the given set function to add an entity to our world
        #https://stackoverflow.com/questions/12435297/how-do-i-jsonify-a-list-in-flask
        data = json.dumps(data) #get the JSON of the data from the request
        #https://stackoverflow.com/questions/7824101/return-http-status-code-201-in-flask
        return data, 200 #return the data of the request in JSON format with status code 200
    except:
        #https://stackoverflow.com/questions/7824101/return-http-status-code-201-in-flask
        #https://stackoverflow.com/questions/12435297/how-do-i-jsonify-a-list-in-flask
        return json.dumps("Error Adding entity to world"), 404

@app.route("/world", methods=['POST','GET'])    
def world():
    '''you should probably return the world here'''
    #https://www.w3schools.com/python/python_try_except.asp
    try:
        #https://stackoverflow.com/questions/12435297/how-do-i-jsonify-a-list-in-flask
        requestedWorld = json.dumps(myWorld.world()) #Get what the world variable contains in JSON format
        #https://stackoverflow.com/questions/7824101/return-http-status-code-201-in-flask
        return requestedWorld, 200 #return the world with status code 200
    except:
        #https://stackoverflow.com/questions/12435297/how-do-i-jsonify-a-list-in-flask
        #https://stackoverflow.com/questions/7824101/return-http-status-code-201-in-flask
        return json.dumps("Error retreiving world"), 500 #500 not 400 not being able to return the world would be a server side error

@app.route("/entity/<entity>")    
def get_entity(entity):
    '''This is the GET version of the entity interface, return a representation of the entity'''
    #https://www.w3schools.com/python/python_try_except.asp
    try:
        #https://stackoverflow.com/questions/12435297/how-do-i-jsonify-a-list-in-flask
        requestedEntity = json.dumps(myWorld.get(entity)) #use the built in get method to get the specific entity and transform it to JSON
        #https://stackoverflow.com/questions/7824101/return-http-status-code-201-in-flask
        return requestedEntity, 200 #return the entity as JSON with status code 200
    except:
        #https://stackoverflow.com/questions/12435297/how-do-i-jsonify-a-list-in-flask
        #https://stackoverflow.com/questions/7824101/return-http-status-code-201-in-flask
        return json.dumps("Error retreiving entity"), 404



@app.route("/clear", methods=['POST','GET'])
def clear():
    '''Clear the world out!'''
    #https://www.w3schools.com/python/python_try_except.asp
    try:
        myWorld.clear() #use the provided method to clear the world
        #https://stackoverflow.com/questions/12435297/how-do-i-jsonify-a-list-in-flask
        #https://stackoverflow.com/questions/7824101/return-http-status-code-201-in-flask
        return json.dumps("World cleared successfully"), 200
    except:
        #https://stackoverflow.com/questions/12435297/how-do-i-jsonify-a-list-in-flask
        #https://stackoverflow.com/questions/7824101/return-http-status-code-201-in-flask
        return json.dumps("World was not cleared successfully"), 500 #500 not 400 not being able to clear the world would be a server side error



if __name__ == "__main__":
    ''' This doesn't work well anymore:
        pip install gunicorn
        and run
        gunicorn -k flask_sockets.worker sockets:app
    '''
    #app.run()
    os.system("gunicorn -k flask_sockets.worker sockets:app")
