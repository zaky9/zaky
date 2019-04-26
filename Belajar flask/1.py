# pip install flask

from flask import request, make_response, abort, Flask, render_template, jsonify #memanggil template dari html, mimbikin jadi json


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')
            

@app.route('/data')
def data():
    return '<h1><i>Andi, Budi, Caca<i></h1>'

# nama = "Andi Susanto"
# usia = 32
profilku = {
    'nama' : "Andi Susanto",
    'usia' : 32
}

@app.route('/about')
def about():
    return render_template(
        'about.html',
        # profil = {
        #     'nama' : nama,
        #     'usia' : usia
        # }
        profil = profilku 
    )

karyawan = [                                # list
    {'id': 1, 'nama': 'Andi', 'usia': 22}, #0
    {'id': 2, 'nama': 'Budi', 'usia': 23}, #1
    {'id': 3, 'nama': 'Caca', 'usia': 24}  #2
]

@app.route('/dict')
def dict():
    return jsonify(karyawan)

@app.route('/dict/<int:numid>') # Calling kariyawan based on the element
def dictnumid(numid):
    
    if numid < 1 or numid > len(karyawan):
        abort(404)
        # return '<h1><i>Maaf data tidak ada<i></h1>'
    else:
        return jsonify(karyawan[int(numid) - 1])

@app.route('/test', methods = ['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'Anda nge-GET'
    elif request.method == 'POST':
        # return 'Anda nge-POST'
        pesanBody = request.json
        print(pesanBody['nama'])    # Menulis di terminal
        return 'Pesan yang anda kirim : ' + pesanBody['nama']
    else:
        return 'Anda tidak nge-GET atau nge-POST'


@app.errorhandler(404)
def notFound(error): #namanya bebas
    # return '<h1>maaf file tidak di temukan</h1>'
    return render_template('error.html')




if __name__ == '__main__':
    app.run(debug = True)       # ngerestart server