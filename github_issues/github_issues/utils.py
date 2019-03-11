#The urllib Library module for access websites.
from urllib.request import urlopen, URLError

#This function check that given URL is valide or not using urllib library
def validate_web_url(url="http://google.com"):
    try:
        urlopen(url)
        return True
    except URLError:
        return False
