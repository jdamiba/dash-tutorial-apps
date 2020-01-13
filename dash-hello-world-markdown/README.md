# Dash Hello World Markdown

## Your Third Dash App

1. Create a folder called `dash-hello-world-markdown` and make it your working directory.
    - `$ mkdir dash-hello-world-markdown && cd dash-hello-world-markdown`
2. Create a file called `app.py`.
    - `$ touch app.py`
3. Fill the contents of `app.py` with the following Python code:
```python
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

text = "# Hello, world!"

app_layout = [dcc.Markdown(children=text), 
             dcc.Markdown(style={"background": "red", "marginLeft": "50px"}, 
                          children='''
                          # A heading.   
                          ## A sub-headingThe top one is ascending.  
                          Regular Text  
                          [a link](https://google.com) 
                          ''')
             ]
                
app.layout = html.Div(children=app_layout)

if __name__ == '__main__':
    app.run_server(debug=True)
```

4. Run the application in your terminal.
    - `$ python app.py`
5. Go to http://127.0.0.1:8050/ with a web browser.
6. If you have trouble creating your own file, try running `$ python app.py` in this directory.

## More Nesting Dash Components

This Dash app demonstrates three things. 

First, it shows how to use the `dcc.Markdown()` component, which a part of the `dash_core_components` library.

Second, it shows how to use a variable as the `children` attribute of a Dash component.

Third, it shows how to create multi-line text blocks inside `dcc.Markdown()` components. 

Fourth, it shows how to style individual components using the `style` parameter. 