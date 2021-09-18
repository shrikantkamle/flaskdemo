from flask import Flask,jsonify
from flask import stream_with_context, request
import json


app = Flask(__name__)



###############################################################
@app.route('/', methods=["GET", "POST"])
def home():
    es = "hi"
    # request_param = json.loads(request.args.get('keyword'))
    # keyword = request_param['keyword']
    # print(request_param,type(request_param))
    if es is not None:
        return '<h1> "Connection successful established!"</h1>'
    else:
        return '<h1> "Connection unsuccessful!!!"</h1>'    

###############################################################