#coding:utf-8

from flask import Flask
from flask import render_template
import os
import string
import glob



app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/myfolkmusic/')
def folkmusic(name=None):
    return render_template('myfolkmusic.html', name=name)
@app.route('/myfolkmusic/<name>')
def myfolkmusic(name=None):
    
   DIR='C://Python34//Scripts//venv//Scripts//templates//static//3130000547//forkmusics//music.txt'
   t=os.listdir(DIR)
   a=[]
  
   for i in range(0,15):
       a.append(t[i][:-4])
       return render_template("nmyfolkmusic.html", name=name,a=a)
@app.route('/illustration/')
def illustation (name=None):
    a=[]
    k=0
    for fn in glob.glob( 'static/3130000547/illusration/illustration.png' + os.sep + '*' ):
        t = os.dirname(fn)
        a.append(t)
    return render_template('illustration.html', name=name)
@app.route('/illustration/<name>')
def myillustation (name=None):
    return render_template('myillustration.html', name=name)

@app.route('/poem/')
def poem (name=None):
    a =[]
    k =0
    for fn in glob.glob( 'static/3130000547/forkmusics/music.png' + os.sep + '*' ):
        t = os.dirname(fn)
        a.append(t)
    return render_template('poem.html', name=name)
@app.route('/poem/<name>')
def mypoem (name=None):
    return render_template('mypoem.html', name=name)


@app.route('/music/')
def music(name=None):
 
    return render_template('music.html', name=name)
@app.route('/about/')
@app.route('/about/<name>')
def aboutme(name=None):
    return render_template('about.html', name=name)
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000, debug=True)  
