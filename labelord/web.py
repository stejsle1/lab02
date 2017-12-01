# This is skeleton for labelord module
# MI-PYT, task 1 (requests+click)
# File: labelord.py
# TODO: create requirements.txt and install

import flask
import getpass
import requests
import click
import configparser
import json
import sys
import os
import hmac
import hashlib

from labelord.setupfile import setup

class LabelordWeb(flask.Flask): 
   """
   Flask web interface class
   """

   def __init__(self, *args, **kwargs): 
      """
      Constructor
      
      :param: ``self`` Context
      :param: ``*args`` Arguments 
      :param: ``**kwargs`` Arguments
      :return: ``None``
      """
      super().__init__(*args, **kwargs)
        # You can do something here, but you don't have to...
        # Adding more args before *args is also possible
        # You need to pass import_name to super as first arg or
        # via keyword (e.g. import_name=__name__)
        # Be careful not to override something Flask-specific
        # @see http://flask.pocoo.org/docs/0.12/api/
        # @see https://github.com/pallets/flask

   def inject_session(self, session):  
        """
        Session setting.
              
        :param: ``self`` Context
        :param: ``session`` Session for comunication with GitHub 
        :return: ``None``
        """
        # TODO: inject session for communication with GitHub
        # The tests will call this method to pass the testing session.
        # Always use session from this call (it will be called before
        # any HTTP request). If this method is not called, create new
        # session.
        self.session = session

   def reload_config(self): 
        """
        Config setting.
        
        Open config file and set congiguration (token, webhook secret, ...), set a self context.
              
        :param: ``self`` Context
        :return: ``None``
        """
        # TODO: check envvar LABELORD_CONFIG and reload the config
        # Because there are problems with reimporting the app with
        # different configuration, this method will be called in
        # order to reload configuration file. Check if everything
        # is correctly set-up
        
        conffile = configparser.ConfigParser()
        conffile.optionxform = str
        
        if 'LABELORD_CONFIG' in os.environ:
           config = os.environ['LABELORD_CONFIG']
           conffile.read(config) 
        else:
           if os.path.isfile('./config.cfg') == True:
              conffile.read('./config.cfg')
              config = './config.cfg'
        
        if os.path.isfile('./config.cfg') == False and 'github' not in conffile:
           print('No GitHub token has been provided', file=sys.stderr)
           sys.exit(3)
        if 'github' in conffile and 'token' not in conffile['github']:
           print('No GitHub token has been provided', file=sys.stderr)
           sys.exit(3)
        else: self.token = conffile['github']['token']
        
        self.session = setup(self.session, self.token)
        
        if 'github' in conffile and 'webhook_secret' not in conffile['github']:
           print('No webhook secret has been provided', file=sys.stderr)
           sys.exit(8)
        else: self.secret = conffile['github']['webhook_secret']
        
        self.repos = []
        if not 'repos' in conffile:
           print('No repositories specification has been found', file=sys.stderr)
           sys.exit(7)      
        for repo in conffile['repos']:
           if conffile.getboolean('repos', repo):
              self.repos.append(repo)  
        
        self.labels = {}
        if 'labels' in conffile:
           for label in conffile['labels']:
              self.labels[label] = conffile['labels'][label]
              
        self.ename = ''
        self.dname = ''                 


# TODO: instantiate LabelordWeb app
# Be careful with configs, this is module-wide variable,
# you want to be able to run CLI app as it was in task 1.
from flask import Flask, current_app, render_template, request, Response, json
app = LabelordWeb(__name__)

# TODO: implement web app
# hint: you can use flask.current_app (inside app context)

@app.template_filter('link')
def convert_time(text):
    """
    Convert the repo name to link, assistant function for GET requests.    
          
    :param: ``text`` String - repository name - to convert
    :return: ``Link``
    """
    return 'https://github.com/' + text

@app.route('/', methods=['GET'])
def get():         
   """
   GET requests
   
   Handle GET requests - print repositories and link to repositories.
         
   :return: ``render template`` Rendering page
   """
   if not current_app.session:
      session = requests.Session()
      current_app.inject_session(session)
   if not current_app.repos:
      current_app.reload_config()   
   return render_template('get.html', repos=current_app.repos)
   
@app.route('/', methods=['POST'])
def post():      
   """
   POST requests   
   
   Handle POST requests - chech if request from GitHub, if do make command according to POST request and send response.
         
   :return: ``response``
   """
   if not current_app.session:
      session = requests.Session()
      current_app.inject_session(session)
   if not current_app.repos:
      current_app.reload_config()
      
   data = json.loads(request.data)
   
   datas = {'hello': 'world', 'number': 3}
   js = json.dumps(datas)
   
   if request.headers['Content-Type'] != 'application/json':
      resp = Response(js, status=200, mimetype='application/json')
      return resp
        
   signature = 'sha1=' + hmac.new(bytes(current_app.secret, encoding="UTF-8"), request.data, hashlib.sha1).hexdigest()
   if not 'X-Hub-Signature' in request.headers or signature != request.headers['X-Hub-Signature']:
      resp = Response(js, status=401, mimetype='application/json')
      return resp
      
   if request.headers['X-GitHub-Event'] != 'ping' and request.headers['X-GitHub-Event'] != 'label':
      resp = Response(js, status=200, mimetype='application/json')
      return resp   
   
   
   
   if request.headers['X-GitHub-Event'] == 'ping':
      resp = Response(js, status=200, mimetype='application/json')
      return resp       
   
   else:
      if data['action'] == 'created':
         if data['repository']['full_name'] not in current_app.repos: 
            resp = Response(js, status=400, mimetype='application/json')
            return resp 
         for repo in current_app.repos: 
            if repo != data['repository']['full_name']:
               colors = json.dumps({"name": data['label']['name'], "color": data['label']['color']})
               list = current_app.session.post('https://api.github.com/repos/' + repo + '/labels', data=colors)
      
      elif data['action'] == 'deleted':
         if data['repository']['full_name'] not in current_app.repos: 
            resp = Response(js, status=400, mimetype='application/json')
            return resp 
         for repo in current_app.repos:
            if repo != data['repository']['full_name'] and current_app.dname != data['label']['name']:
               list = current_app.session.delete('https://api.github.com/repos/' + repo + '/labels/' + data['label']['name'])
         # TODO
         current_app.dname = data['label']['name']
      
      elif data['action'] == 'edited':  
         if data['repository']['full_name'] not in current_app.repos: 
            resp = Response(js, status=400, mimetype='application/json')
            return resp 
         for repo in current_app.repos:
            if 'name' not in data['changes'] or 'from' not in data['changes']['name']:
               colorname = data['label']['name']    
            else: colorname = data['changes']['name']['from']   
            if repo != data['repository']['full_name'] and current_app.ename != data['label']['name']:
               colors = json.dumps({"name": data['label']['name'], "color": data['label']['color']})
               list = current_app.session.patch('https://api.github.com/repos/' + repo + '/labels/' + colorname, data=colors)
         # TODO
         current_app.ename = data['label']['name']
         
      resp = Response(js, status=200, content_type='application/json', mimetype='application/json')
      resp.headers['Link'] = 'https://api.github.com/'
       
      return resp
