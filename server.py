from flask import Flask, render_template, request, jsonify
import sqlalchemy as db
import json
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
#from code_blocks import *


app = Flask(__name__)


res = []
req = []
file_name = 'main'
token = '925344997:AAGWfYn_GkgWBd1ViHdp6KcYmhG51yKSjJQ'

client = app.test_client()

engine = create_engine('sqlite:///Users.sqlite')

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

base = declarative_base()
base.query = session.query_property()

from models import *

base.metadata.create_all(bind=engine)


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')


@app.route('/post', methods=['GET', 'POST'])
def make_instruction():
    try:
        JSON_sent = request.get_json('data')
        print(JSON_sent)
        data = json.dumps(JSON_sent)
        print(data)
        with open('Instructions Example.txt', 'w') as instructions:
            instructions.write("token 12345 \n")
            instructions.write("start\n")
            instructions.write("start_message Hello, thanks for starting me \n")
            for i in range(len(JSON_sent['res_btn'])):
                instructions.write('make_button  ""' + JSON_sent['res_btn'][i] + '"" ""' + JSON_sent['req_btn'][i] + '""\n')
            for i in range(len(JSON_sent['res_msg'])):
                instructions.write('text_response ""' + JSON_sent['res_msg'][i] + '"" ""' + JSON_sent['req_msg'][i] + '""\n')
            instructions.write("end\n")
            #start()
        return jsonify('OK')
    except Exception as e:
        print("AJAX excepted " + str(e))
        return str(e)


@app.route('/', methods=['GET', 'POST'])
def get_content():
    print(request.form.get('request'))


app.run(debug=True)
