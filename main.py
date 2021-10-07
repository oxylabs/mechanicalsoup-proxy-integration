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
        browser.open("https://ip.oxylabs.io/") 
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
