# Oxylabs’ Residential Proxies integration with MechanicalSoup

[<img src="https://img.shields.io/static/v1?label=&message=Python&color=brightgreen" />](https://github.com/topics/python) [<img src="https://img.shields.io/static/v1?label=&message=Mechanical%20Soup&color=orange" />](https://github.com/topics/mechanicalsoup) [<img src="https://img.shields.io/static/v1?label=&message=Web-Scraping&color=yellow" />](https://github.com/topics/web-scraping) [<img src="https://img.shields.io/static/v1?label=&message=Rotating%20Proxies&color=blueviolet" />](https://github.com/topics/rotating-proxies)

[Mechanical Soup](https://github.com/MechanicalSoup/MechanicalSoup) is a Python library designed
for automating web interactions such as submitting forms, following links and redirects. Since it
is built on using Python `requests` and `BeautifulSoup` libraries, `MechanicalSoup` 
is often used as a library to perform some web-scraping operations, such as image extraction,
due to the powerful integrated functions that comes in with it. In this tutorial, we're going
to cover how you can integrate Oxylabs' Residential Proxies with MechanicalSoup and share a code
sample for submitting an HTML form while using proxies.

## Requirements

For the integration to work, you'll need to install it on your system. 
You can do it using `pip` command:
```bash
pip install mechanicalsoup
```
`Python 3` or higher<br>

Residential Proxies: https://oxylabs.io/products/residential-proxy-pool

## Proxy Authentication
For proxies to work, you'll need to specify your account credentials inside the 
[main.py](https://github.com/oxylabs/mechanicalsoup-proxy-integration/blob/main/main.py) file:

```python
USERNAME = "your_username"
PASSWORD = "your_password"
HOST = "pr.oxylabs.io"
PORT = 7777
```
Adjust the `your_username` and `your_password` fields with the username and password 
of your Oxylabs account.

## Testing Proxy Connection
To see if the proxy is working, try visiting ip.oxylabs.io. <br>If everything is working correctly, 
it will return an IP address of a proxy that you're using.

## Identifying an HTML form
Identifying an HTML form in MechanicalSoup is relatively easy - all you have to do is to locate it
via CSS selector using a `select_form` method. It returns a `soup` object that can be later 
retrieved using `form` attribute. Here's an example of locating a form and printing its input fields.
```python
import sys

import mechanicalsoup

USER = "your_username"
PASSWORD = "your_password"
END_POINT = "pr.oxylabs.io:7777"

proxies = {
"http": f"http://{USER}:{PASSWORD}@{END_POINT}",
"https": f"http://{USER}:{PASSWORD}@{END_POINT}"
}

browser = mechanicalsoup.StatefulBrowser()
browser.session.proxies = proxies 

def foo():
    try:
        browser.open("https://httpbin.org/forms/post") 
    except Exception:
        exc_type, value, traceback = sys.exc_info()
        return f"{exc_type.__name__}: Wrong account credentials!"

    # Selecting a form in HTML using a CSS Selector
    form = browser.select_form('form[action="/post"]')
    # Printing the form
    return browser.form.print_summary()

if __name__ == "__main__":
    print(foo())

```

## Full Code: Submitting an HTML Form with Proxies
```python
import sys

import mechanicalsoup

# Credentials of your Oxylabs' account
USER = "your_username"
PASSWORD = "your_password"
END_POINT = "pr.oxylabs.io:7777"

proxies = {
"http": f"http://{USER}:{PASSWORD}@{END_POINT}",
"https": f"http://{USER}:{PASSWORD}@{END_POINT}"
}

# Initiating a MechanicalSoup object
browser = mechanicalsoup.StatefulBrowser()
browser.session.proxies = proxies 

def foo():
    try:
        browser.open("https://httpbin.org/forms/post") 
    except Exception:
        exc_type, value, traceback = sys.exc_info()
        return f"{exc_type.__name__}: Wrong account credentials!"

    # Selecting a form in HTML using a CSS Selector
    form = browser.select_form('form[action="/post"]')

    form_info = {
        "custname": "Jonas",
        "custtel": "123",
        "custemail": "info@example.com",
        "size": "small",
        "topping": ("bacon", "cheese", "onion"),
        "delivery": "18:30",
        "comments": "I like pizza"
    }

    # Iterating over a dictionary object (form_info) 
    # to populate the form fields with the defined values
    for key, value in form_info.items():
        form.set(key, value)

    # Launching a Browser
    browser.launch_browser()
    response = browser.submit_selected()
    return response.text

if __name__ == "__main__":
    print(foo())
```
If you're having any trouble integrating proxies with MechanicalSoup and this guide didn't help 
you - feel free to contact Oxylabs customer support at support@oxylabs.io.
