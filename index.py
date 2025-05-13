from flask import Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1> Primer Aplicación Web </h1>"