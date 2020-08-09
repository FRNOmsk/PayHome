from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8000)
CGIHTTPRequestHandler.cgi_directories = '/cgi-bin'
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()