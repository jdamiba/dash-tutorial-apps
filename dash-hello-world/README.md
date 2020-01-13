# Dash Hello World

## Your First Dash App

1. Create a folder called `hello-world` and make it your working directory.
    - `$ mkdir hello-word && cd hello-world`
2. Create a file called `app.py`.
    - `$ touch app.py`
3. Fill the contents of `app.py` with the following Python code:
```python
import dash
import dash_html_components as html

app = dash.Dash(__name__)
                
app.layout = html.H1(children="Hello, world!")

if __name__ == '__main__':
    app.run_server(debug=True)
```
4. Run the application in your terminal.
    - `$ python app.py`
5. Go to http://127.0.0.1:8050/ with a web browser.
6. If you have trouble creating your own file, try running `$ python app.py` in this directory.

## What Just Happened?

The code in `app.py` does two things.

First, it initializes a Dash app that will persist for as long as the program is running. You can stop the Dash app by hitting `Control + C` in the same terminal ran `$ python app.py`.

Second, it defines the `layout` of the Dash app. This is used behind the scenes to build the HTML, CSS, and JavaScript files that are sent to web browsers when they make a request. 

In this case we're using an open source Dash component from the `dash_html_components` library, `html.H1()`, to define the `layout`. As you might have guessed from its name, this Dash component renders an HTML h1 tag. Other components in the `dash_html_components` library render the other HTML tags.

You can use open-source Dash components like `html.H1()` to build layouts for Dash apps and you can make your own Dash components.

Go to /dash-html-nesting to learn how to build more complex layouts by nesting Dash components.



