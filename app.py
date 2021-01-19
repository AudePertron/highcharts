from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort
from data import quotidien_oui, quotidien_non, personnel_oui, personnel_non, chauffage_oui, chauffage_non

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


@app.route('/')
def recup_stats():

    return render_template("index.html", quotidien_oui=quotidien_oui, quotidien_non=quotidien_non, personnel_oui=personnel_oui,
        personnel_non=personnel_non, chauffage_oui=chauffage_oui, chauffage_non=chauffage_non)
