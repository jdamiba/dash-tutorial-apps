# Dash Hello World

## Line 4
Dash apps are web servers built in Python. 

When you define your app's `layout`, you are telling the web server how to respond to web clients that make HTTP requests to it. 

By default, Dash assumes that you want the `layout` of your app to define how the web server should respond to an incoming HTTP GET request to the root URL where the web server lives. 

In your development environment, that root URL is going to be http://127.0.0.1:8050/ because Dash exposes a web server on port 8050 locally. 

In other words, whatever you define as the app's `layout` will be sent as a response to web browsers that navigate to the URL http://127.0.0.1:8050/ on your computer. 

When you deploy your Dash app (for example to Heroku), the web server will do the same thing by default- use the `layout` you have defined to respond to incoming requests to its root URL. However, when you deploy, the root URL is going to be whatever your domain name is (ie https://www.example-url-doesnt-exist.herokuapps.com). 

This is a key concept to understand while developing Dash apps. 

The `layout` of an application defines how the application responds to incoming HTTP GET requests to the root directory of the environment where the web server is running. 

That could be your computer's `localhost` when you're developing an application locally, or a virtual machine run by your web hosting company when you deploy your application.

# Line 6 

The fastest way to define a `layout` for your app is to use the built-in `dash_html_components` library to define the HTML structure. 

In this example, we are using the `html.H1()` function. Any text you pass to this function gets rendered inside an `<h1>` tag.

To see a list of all the 