from flask import redirect, url_for, request, Flask, send_from_directory, render_template
app = Flask(__name__, static_url_path='')

data = {
    'nama' :'Andi',
    'pwd' : '12345'
}

#home route
@app.route('/')
def home():
    return '<h1>Welcome to my web server!</h1>'

#render template html
@app.route('/login')
def html():
    return render_template('html.html')

#POST route
@app.route('/post',methods = ['POST'])
def post():
    nam = request.form['nama'] 
    pwd = request.form['pass']
    print('Nama: ', nam, 'Pass: ', pwd)
    # return 'Nama: ' + nam + ' Pass' + pwd

    # if nam == data['nama'] and pwd == data['pwd ']:
    #     return redirect(url_for('sukses', nama = nam))
    # else:

        
    # data = request.json
    # print('Anda ngirim ini: ' + data['nama'] + data['pass'])
    # return 'Anda ngirim ini: ' + data['nama'] + data['pass']

@app.route('/sukses/<string:nama>')
def sukses(nama):
    return '<h1>Selamat datang ' + nama + '</h1>' 

# @app.route('/gagal')
# def gagal(nama):
#     return '<h1> Coba lagi '

# render static file =>localhost:5000/images/foto/score.png
@app.route('/images/<path:path>')   #nama rute
def staticfile(path):
    return send_from_directory('images', path) #folder name

#404 route
@app.errorhandler(404)
def error404(error):
    return '<h1>Error: 404 Not Found</h1>'

if __name__ == "__main__":
    app.run(debug = True)