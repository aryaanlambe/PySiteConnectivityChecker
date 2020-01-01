# Original credits go to @yasinkuyu
# Remember to install the requests package using pip3 first.

def check_internet():
    url = input("Enter URL to Test Connection. \n Remember to include the http:// as well. ")
    timeout = 5
    try:

        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print ("Failed to Test: No Internet connection.")
    return False