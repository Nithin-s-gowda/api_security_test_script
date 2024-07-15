import requests

#Function to test for sql injection
def test_sql_injection(url):
    #payload that might cause SQL error if improperly handled
    payload = '" OR \'1\'=\'1'
    params = {'input': payload}
    response = requests.get(url, params=params)

    if "SQL syntax" in response.text:
        print("Potential SQL injection vulnerability found")
    else:
        print("no obvious SQL injection vulnerability detected")

#funtion to test for XSS
def test_xss(url):
    #simple script tag payload
    payload = "<script>alert('XSS')</script>"
    params = {'input':payload}
    response = requests.get(url, params=params)

    if payload in response.text:
        print("potential XSS vulnerability found")
    else:
        print("no obvious XSS vulnerability detected")
    
#function to test for Misconfiguration
def test_misconfiguration(url):
    response = requests.get(url)

    #chect for insecure headers or too mach information in error messages
    if 'X-Powered_By' in response.headers or 'Server' in response.headers:
        print("potential misconfiguration found (informatiove headers)")
    else:
        print("no obvious misconfiguration detected")

#main function to run our tests
def main():
    url = input("enter th URL of the API endpoint ot test: ")
    print("\n Testing for SQL injection..")
    test_sql_injection(url)

    print("\ntesting for XSS..")
    test_xss(url)

    print("\nTesting for Misconfiguration..")
    test_misconfiguration(url)

if __name__ == "__main__":
    main()