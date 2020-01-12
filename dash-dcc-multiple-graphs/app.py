import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import re

# Use our own Markdown function so that we can
# use `relpath` for the embedded URLs
def Markdown(children='', **kwargs):
    children = re.sub(
        ']\((\/\S*)\)',
        children
    )
    return dcc.Markdown(children=children, **kwargs)

app = dash.Dash(__name__)

fig = px.scatter(x=[1,2,3,4,5], y=[1,2,3,4,5])

fig2 = px.scatter(x=[1,2,3,4,5], y=[5,4,3,2,1])

app.layout = html.Div(children=[
    dcc.Markdown(children="Below are two figures built with Plotly Express."),
    dcc.Graph(figure=fig),
    dcc.Graph(figure=fig2)
])

if __name__ == '__main__':
    app.run_server(debug=True)
