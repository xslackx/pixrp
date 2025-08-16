from flask import Flask, request
from genpix import tx_user

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>usage: /pix?txid= /p>"

@app.route('/pix', methods=['GET'])
def generate_static_pix():
    user_txid = request.args.get('txid')
    if user_txid:
        return tx_user(user_txid)
    return
    
