import dash
import dash_html_components as html

app = dash.Dash(__name__)
                
app.layout = html.Div(children=[
    html.H1(children="Hello, world!"),
    html.Div(children="This is my second Dash app!")
])

if __name__ == '__main__':
    app.run_server(debug=True)
