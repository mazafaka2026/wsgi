import urlparse
slovar=''
def app (environ, start_response):
	environ=arg
	status='200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	body=slovar
	start_response(status, headers)
	return[body]
	

url = "http://example.com/?a=1&a=2&c=123&d=6&a=10"
print url
query = urlparse.urlparse(url).query
url2=query.split("&")


#params = urlparse.parse_qs(query)
#print params

for arg in url2:
	print arg
