# retrieve data from the internet
import urllib.request


sample_url = "http://httpbin.org/xml"

# TODO: Create a request to retrieve data using urllib.request
response = urllib.request.urlopen(sample_url)

# TODO: Check the status
status_code = response.status
print(status_code)


# TODO: if no error, then read the response contents
if status_code >= 200 and status_code < 300:
    # TODO: work with response headers
    print(response.getheaders())
  

    print("------------------------------------------------------------------------")

    data = response.read()
    print(data)
    
    print("------------------------------------------------------------------------")
    
    data_utf = data.decode('utf-8')
    print(data_utf)

