import os
from flask import  request,flash
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS={'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

        
def upload_file(app):
    if 'file' not in request.files:
        flash("No file part")
    file=request.files['file']
    if file.filename=='':
        flash('No file selected')   
    if file and allowed_file(file.filename):
     filename = secure_filename(file.filename)
     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
     return "file uploaded successfully"
     # return redirect(url_for('download_file', name=filename))  