from app import app
@app.route('/')
@app.route('/index')
def index():
    return """<html>
            <head><title>GURSIMRAN WEBPAGE</TITLE>
            </head>
            <body>
            hello!!!
            aa thu
            other name of gurneet
            </body>
            </html>"""
