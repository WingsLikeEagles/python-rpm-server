#!/usr/bin/python3
from os import chdir
from http.server import HTTPServer, CGIHTTPRequestHandler
from ssl import wrap_socket

# this is the folder where you need to store your files to be served.
files='/web/files'
chdir(files)

port=443

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)

httpd.socket = wrap_socket (httpd.socket,
        keyfile="/certs/key.pem",
        certfile='/certs/cert.pem', server_side=True)

print('Starting server on port ', port)

httpd.serve_forever()
