from flask import render_template, Flask, request
app = Flask(__name__)
import os,glob,sys
from bs4 import BeautifulSoup
import urllib2

@app.route('/')
def index():
        return render_template("index.html")

def turn_s(n):
	if (n <= 9):
		return ("00%d"%n)
	if (n <= 99):
		return ("0%d"%n)
	return ("%d"%n)

def count_n(i):
	n = 1
	while (os.path.exists("static/text%s/%s.txt"%(i,turn_s(n)))):
		n = n + 1
	return (n)

def have(name,n,i):
	for j in range(n-1):
		file_obj = open('static/text%s/%s.txt'%(i,turn_s(j+1)))
		ff = file_obj.readline().decode("utf-8")[:-1]
		if (ff == name):
			return True
	return False

def get_music_res(url):
	content = urllib2.urlopen(url)
	soup = BeautifulSoup(content, "html.parser")
	n = count_n("")
	for span in soup.find_all('span',class_="song-title "):
		name = span.a.get_text()
		if (len(name) > 28):
			continue
		if have(name,n,''):
			continue
		num = span.a['href'][6:]
		mp3 = urllib2.urlopen('http://music.baidu.com/data/music/file?link=&song_id=%s'%num).read()
		if (len(mp3) < 1000000):
			continue
		with open("static/music/%s.mp3"%turn_s(n), "wb") as code:
			code.write(mp3)
		try:
			content2 = urllib2.urlopen('http://music.baidu.com/song/%s'%num)
		except urllib2.HTTPError:
			continue
			# print(v)
		content2 = urllib2.urlopen('http://music.baidu.com/song/%s'%num)
		soup2 = BeautifulSoup(content2, "html.parser")
		a = soup2.find('a', class_="down-lrc-btn")
		if not(a):
			continue
		url2 = a['data-lyricdata'][11:]
		url2 = "http://music.baidu.com/%s"%(url2[:-3])

		f = open("static/text/%s.txt"%turn_s(n),'w')
		f.write(name.encode("utf-8"))
		f.write("\n\n")
		f.write(urllib2.urlopen(url2).read())
		f.close()
		n+=1

@app.route('/music')
def music():
	a = [[] for i in range(5)]
	k = 0
	for fn in glob.glob( 'static/text' + os.sep + '*' ):
		fn = fn[-7:-4]
		f = open('static/text/%s.txt'% fn,'r')
		a[k].append({'nb':fn, 't':f.readline()})
		k = (k + 1) % 5
	return render_template("myforkmusic.html", a = a)


@app.route('/music/<name>')
def AnimePlay():
	num = request.args.get('num')
	return render_template("music.html",name=name,num = num)



if __name__ == '__main__':
	get_music_res('http://music.baidu.com/top/new')
	app.run(host="127.0.0.1",port=5000,debug=True)
