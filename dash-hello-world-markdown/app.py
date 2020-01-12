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
