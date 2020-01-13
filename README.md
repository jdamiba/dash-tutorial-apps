# Building Web Servers With Python

## What is a web server?

Web servers allow for a distributed Internet by freeing users from the burden of having to store copies of the websites they want to visit on their computer's hard drive. Since there are so many websites, users would have to manage a ton of hard drives if they had to carry around copies of the Internet.

Instead of storing local copies of websites, web browsers make requests for the files they want to web servers using URLs and the HTTP protocol.

Web servers parse incoming HTTP requests from different web browsers and respond to each request with the files the web browser needs to build the site it requested. These are generally HTML, CSS, and JavaScript files but could also include data like JSON, videos, or pdfs.

### Request/Response Example 

1. A web browser sends a request for the URL https://www.google.com to Google's web server using the HTTP protocol
2. The request is routed to Google's web server 
3. Google's web server parses the incoming request to make sure it's valid. Asks questions like: 
    - Is the request properly formatted?
        - The HTTP protocol is very specific about how web browsers should make requests. Requests will fail if they don't adhere to the protocol.
    - Does the requested URL exist?
        - Web browsers often request URLs that do not exist on the web server. This can be because a URL is misspelled or because a resource has moved from one URL to another.
    - Does the web browser have access to the files stored at the URL?
        - The request might come from a blacklisted IP address.
4. If the request is valid, Google's web server responds with HTML, CSS, and JavaScript files that the web browser will use to create the Google home page. 
5. The response is routed back to the web browser
6. The web browser parses the HTML, CSS, and JavaScript files it and makes the Google homepage.
7. After a user types a query and hits Search in their web browser, the web browser sends another request to the Google web server. 
    - The second request also includes the search query in the URL that is requested, which the Google web server will use to respond to that request with HTML, CSS, and JavaScript files that the web browser uses to create the Google search results page.

## How Can You Make Web Servers?

You can make web servers using Dash, an open-source framework for making web servers with Python. With Dash, you write Python programs known as Dash apps that are web servers capable of interacting with web browsers.

1. To make Dash apps, you will use the Python programming language. This requires installing Python on your computer if you don't already have it. You also need a way of installing Python packages in your Python environment and a code editor. 
    - [official downloading python page](https://wiki.python.org/moin/BeginnersGuide/Download)
    - [pip](https://pip.pypa.io/en/stable/installing/) and [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) are popular Python package managers 
    - VS Code is a great free code editor

2. In the Python environment of your choice, install the following packages so that they are accessible to your Dash apps:
    - [`dash`](https://dash.plot.ly/)
    - [`dash_core_components`](https://dash.plot.ly/dash-core-components)
    - [`dash_html_components`](https://dash.plot.ly/dash-html-components)
    - the [`plotly.py`](https://plot.ly/python/) graphing library (includes [`plotly.express`](https://plot.ly/python/plotly-express/) built-in)
    - You can do this achieved using `pip` or other Python package managers in your terminal. For example:
        - `$ pip install dash dash_core_components dash_html_components plotly`

4. Go to /hello-world to get started making Dash apps. 