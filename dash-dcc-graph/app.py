import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

app = dash.Dash(__name__)

fig = px.scatter(x=[1,2,3,4,5], y=[1,2,3,4,5])

app.layout = html.Div(children=[
    dcc.Markdown(children="This is a scatter plot built with Plotly Express:"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
