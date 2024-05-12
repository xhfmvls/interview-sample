from flask import render_template, render_template_string, request
from app import app
import requests

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    team_members = [
        {'name': 'John Doe', 'role': 'Founder'},
        {'name': 'Jane Smith', 'role': 'Developer'},
        {'name': 'Alice Johnson', 'role': 'Designer'}
    ]
    return render_template('about.html', title='About Us', team_members=team_members)

@app.route('/search')
def search():
    search_query = request.args.get('search')
    html_template = """
    <p>You searched for: "{}"</p>
    """
    return render_template_string(html_template.format(search_query))