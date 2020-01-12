import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    dcc.Markdown(children="# Hello, world!"),
    dcc.Markdown(children="Lorem ipsum."),
    dcc.Markdown(children="## Another heading.")
])

if __name__ == '__main__':
    app.run_server(debug=True)
