from os import path
from pathlib import Path
import sys
from flask import Flask, render_template
from flask_frozen import Freezer

template_folder = path.abspath('./wiki')

app = Flask(__name__, template_folder=template_folder)
app.config['FREEZER_DESTINATION'] = 'public'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)

@app.cli.command()
def freeze():
    freezer.freeze()

@app.cli.command()
def serve():
    freezer.run()

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/<page>')
def pages(page):
    return render_template(str(Path('pages')) + '/' + page.lower() + '.html')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'freeze':
        freezer.freeze()
    elif len(sys.argv) > 1 and sys.argv[1] == 'serve':
        freezer.run()
    else:
        app.run(host='0.0.0.0', port=8080)