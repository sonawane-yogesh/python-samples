from flask import Blueprint

project_bp = Blueprint('projects', __name__)


@project_bp.route('/get-all/')
def hello():
    projects=mongo.db.MongoProjectMaster.find()
    return projects
