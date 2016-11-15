from flask import Flask, render_template, session
import api
import os

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

# Register the controllers
app.register_blueprint(api.api)

# set the secret key.  keep this really secret:
app.secret_key = "\x86\xa8\x0b\xfe\x0c.\xeb\xe9\xb3\x870QGG\xaay\x1d\x84\xd5F\xa3A\xd0\x88"

# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='localhost', port=3000, debug=True)
