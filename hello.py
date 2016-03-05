import urlparse
slovar=''
def app (environ, start_response):
	url=''#environ['QUERY_STRING']
	print url
	query = urlparse.urlparse(url).query
	url_fix=query.split("&")
	for slovar in url_fix:
		print 'fix_url---'+ slovar
	
	status='200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	body=slovar
	print 'body.....'+body
	start_response(status, headers)
	if url == '':
		print 'bed'
	else:
		print ''
		print url
		query = urlparse.urlparse(url).query
		url_fix=query.split("&")
		for slovar in url_fix:
			print 'fix_url---'+ slovar
			body=slovar
			return[body]
	#return[body]
	
print 'Hello'
