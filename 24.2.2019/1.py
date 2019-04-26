from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './storage'

# home route
@app.route('/')
def home():
    return render_template('home.html')

# new route
@app.route('/new')
def new():
    return render_template('new.html')

# upload route
@app.route('/upload', methods=['POST'])
def upload():
    data = request.files['file']
    namafile = secure_filename(data.filename) #mendapatkan file name
    data.save(os.path.join(app.config['UPLOAD_FOLDER'], namafile))
    # print(data)
    # return redirect('/storage/' + namafile)
    return redirect('/sukses/'+ namafile)

@app.route('/storage/<filename>')
def send_file(filename):
    return send_from_directory('./storage', filename)

# after upload = render static file
# @app.route('/storage/<path:path>')
# def suksesUpload(path):
#     return render_template('uploaded.html')
    # send_from_directory('storage',path)

    
    # request.files   # merequest file data
    # request.from    # Merequest langsung dari html
    # request.json    # Merequest json data
@app.route('/sukses/<filename>')
def sukses(filename):
    filename = 'http://localhost:5000/storage/'+ filename
    return render_template('uploaded.html', nama = filename)
    
# Error handler
@app.errorhandler(404)
def notfound404(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug = True)