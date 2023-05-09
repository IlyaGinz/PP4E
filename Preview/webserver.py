import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 8080
os.chdir(webdir)
srvaddr = ("127.0.0.1", port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()