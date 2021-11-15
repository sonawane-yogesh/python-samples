from logging import debug
from flask import Flask
import flask
from flask import json
from flask_pymongo import PyMongo
from bson import json_util
from home import home_bp
from contact import contact_bp
from project import project_bp
from server import get_projects, insertProject
from upload_file import upload_file

app = Flask(__name__)
UPLOAD_FOLDER="D:\\python-samples\\uploads"
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
# app.config["MONGO_URI"]="mongodb://localhost:28000/fkreqpkgdb"
#mongo = PyMongo(app)

mongodb_client = PyMongo(app, uri="mongodb://localhost:28000/fkreqpkgdb")
db = mongodb_client.db

app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(contact_bp, url_prefix='/contact')
app.register_blueprint(project_bp, url_prefix='/projects')


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/get-projects/', methods=['GET'])
def getprojects():
    response = get_projects()
    data = json.dumps(response, default=json_util.default)
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json',
        content_type='application/json'
    )
    return response


@app.route("/add-project", methods=["POST"])
def addProject():
    project = flask.request.json
    doc = insertProject(project)
    #result=json.dumps([doc.inserted_id],default=json_util.default)
    response = app.response_class(
       response=doc.inserted_id,
        status=200,
        content_type='application/json'
    )
    return response


@app.route("/upload-file",methods=["post"])
def uploadFile():
    msg=upload_file(app)  
    return msg

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=10050)
