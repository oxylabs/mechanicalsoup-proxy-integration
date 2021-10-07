import mechanicalsoup

# Credentials of your Oxylabs' account.
USER = "your_username"
PASSWORD = "your_password"
END_POINT = "pr.oxylabs.io:7777"

proxies = {
    "http": f"http://{USER}:{PASSWORD}@{END_POINT}",
    "https": f"http://{USER}:{PASSWORD}@{END_POINT}",
}

def get_html_form(proxies):
    # Initiate a MechanicalSoup object.
    browser = mechanicalsoup.StatefulBrowser()
    browser.session.proxies = proxies 
    try:
        browser.open("https://httpbin.org/forms/post") 
    except Exception as e:
        return e

    # Select a form in HTML using a CSS Selector.
    form = browser.select_form('form[action="/post"]')

    form_info = {
        "custname": "Jonas",
        "custtel": "123",
        "custemail": "info@example.com",
        "size": "small",
        "topping": ("bacon", "cheese", "onion"),
        "delivery": "18:30",
        "comments": "I like pizza",
    }

    # Iterate over a dictionary object (form_info) 
    # to populate the form fields with the defined values.
    for key, value in form_info.items():
        form.set(key, value)

    # Launch a Browser.
    browser.launch_browser()
    response = browser.submit_selected()
    return response.text

if __name__ == "__main__":
    print(get_html_form(proxies))
