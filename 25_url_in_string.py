import re

str = "im blogger at http://www.google.com/ and http://www.Facebook.com"

# https://urlregex.com/
URL_PATTERN = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

url = re.findall(URL_PATTERN,str)

print(url) 