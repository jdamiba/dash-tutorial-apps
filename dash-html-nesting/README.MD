# Dash HTML Nesting 

Nesting Dash components enables you to build more complex layouts for your Dash apps.

## Your Second Dash App

1. Create a folder called `dash-html-nesting` and make it your working directory.
    - `$ mkdir dash-html-nesting && cd dash-html-nesting`
2. Create a file called `app.py`.
    - `$ touch app.py`
3. Fill the contents of `app.py` with the following Python code:
```python
import dash
import dash_html_components as html

app = dash.Dash(__name__)
                
app.layout = html.Div(children=[
    html.H1(children="Hello, world!"),
    html.Div(children="This is my second Dash app!")
])

if __name__ == '__main__':
    app.run_server(debug=True)
```
4. Run the application in your terminal.
    - `$ python app.py`
5. Go to http://127.0.0.1:8050/ with a web browser.
6. If you have trouble creating your own file, try running `$ python app.py` in this directory.

## Nesting Dash Components

A common pattern for creating layouts in Dash apps is to create a top-level `html.Div()` Dash component whose `children` attribute is a Python list that contains Dash components. 

In this example, the `children` attribute of the top-level `html.Div()` Dash component is a list of two Dash components.

To learn more about nesting Dash components, go to /dash-hello-world-markdown.