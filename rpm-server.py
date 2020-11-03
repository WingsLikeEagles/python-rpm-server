#!/usr/bin/python3
from os import chdir
from http.server import HTTPServer, CGIHTTPRequestHandler
# this is the folder where you need to store your files to be served.
files='./files'
chdir(files)
# This is the port you want to listen for requests
port=80
server_object = HTTPServer(server_address=('',port),
RequestHandlerClass=CGIHTTPRequestHandler)
print('Starting server on port ', port)
server_object.serve_forever()
