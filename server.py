from flask import Flask, render_template
from classax.app import classax_bp
from composers.app import composers_bp
# import os

server = Flask(__name__, static_folder='', template_folder='')
server.register_blueprint(classax_bp, url_prefix='/classax')
server.register_blueprint(composers_bp, url_prefix='/composers')

@server.route("/")
def main():
  return render_template("home.html")

if __name__ == '__main__':
#  server.run(host="0.0.0.0", port=443, ssl_context='adhoc', debug=True)
  server.run(host='0.0.0.0',
             port=443,
             ssl_context=('/etc/letsencrypt/live/www.chrimson.net/fullchain.pem',
                          '/etc/letsencrypt/live/www.chrimson.net/privkey.pem'),
             debug=True)

