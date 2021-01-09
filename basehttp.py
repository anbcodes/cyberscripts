import urllib.request

req = urllib.request.Request("[URL]")
# Missing a whole chunk of code here!
response = urllib.request.urlopen(req)
response = response.read()

print(response)