# Using the URL parsing functions
import urllib.parse

sample_url = "http://server.example.com:8080/example.html?val1=1&val2=Hello+World"

# TODO: parse a URL with urlparse()
result = urllib.parse.urlparse(sample_url)
print(result)

# TODO: process the query part of the URL with parse_qs()
# returns dict of lists
querystr = urllib.parse.parse_qs(result.query)
print(querystr)

# TODO: parse the query string using parse_qsl()
# returns list of tuples
querystr = urllib.parse.parse_qsl(result.query)
print(querystr)

# TODO: create the URL with the geturl() method
print(result.geturl)
print()

# TODO: quote() replaces special characters for use in URLs
sample_string = "Hello El Niño"
print(urllib.parse.quote(sample_string))
print(urllib.parse.quote_plus(sample_string))

# TODO: Use urlencode() to convert maps to parameter values
query_data = {
    'Name': "John Doe",
    "City": "Anytown USA",
    "Age": 37
}
result = urllib.parse.urlencode(query_data)
print(result)
