import dash
from dash import Dash, html
from flask import Flask, redirect, request

server = Flask(__name__);
app = Dash(__name__, server=server, use_pages=True)

@server.before_request
def index_redirect():
    if request.path == '/':
        return redirect('/inicio')

app.layout = html.Div([ dash.page_container ])

if __name__ == "__main__":
    app.run(debug=True)

"""

    html.H1("Golden Dashboard App"),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
"""