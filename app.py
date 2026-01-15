from flask import Flask, request
from genpix import tx_user
from dotenv import dotenv_values
from flask_cors import CORS

app = Flask(__name__)
yes = { **dotenv_values('.cors') }
cors = CORS(app, resources=yes["allow"],
            max_age="10",
            methods=["GET"])

@app.route("/")
def hello_world() -> str:
    return "<p>usage: /pix?txid=RP4205F31626541746F653CBAD3VBECDBAX&value=1/p>"

@app.route('/pix', methods=['GET'])
def generate_static_pix() -> dict:
    user_txid = request.args.get('txid')
    user_value = request.args.get('value')
    if user_txid and user_value:
        return {
                "status": 'ok', 
                'code': tx_user(user_txid,user_value)
                }
    else: 
        return {"status": "fail", "code": ""}
    
