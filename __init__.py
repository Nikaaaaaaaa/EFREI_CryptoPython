from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('')
  
@app.route('/de_6_faces.html')
def de6f():
    return render_template('De_6_Faces.html')
  
@app.route('/bibliotheque_images.html')
def bbtimg():
    return render_template('bibliotheque_images.html')

@app.route('/roulette_russe.html')
def rrusse():
    return render_template('rouletterusse.html')

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
