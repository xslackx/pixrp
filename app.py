from flask import Flask, request
from genpix import tx_user

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>usage: /pix?txid=RP4205F31626541746F653CBAD3VBECDBAX&value=1/p>"

@app.route('/pix', methods=['GET'])
def generate_static_pix():
    user_txid = request.args.get('txid')
    user_value = request.args.get('value')
    if user_txid and user_value:
        return tx_user(user_txid, user_value)
    return
    
