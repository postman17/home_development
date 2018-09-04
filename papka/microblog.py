from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import json
import os

app.config['DEBUG'] = True

def iter_files():
    list_files = []
    l_files = os.listdir(path='posttext')
    for file in l_files:
        f = open('posttext/'+file)
        cont = f.read()
        jpost = json.loads(cont)
        list_files.append(jpost)
        f.close()
    return list_files

def add_file(title, content):
    list_files = os.listdir(path='posttext')
    end_list = list_files[(len(list_files)-1)]
    f_list = str(int(end_list)+1)
    with open('posttext/'+f_list, mode='w') as f:
        f.write(r'{"title":"')
        f.write(title)
        f.write(r'","content":"')
        f.write(content)
        f.write(r'"}')

@app.route('/')
def index():
    posts = iter_files()
    print(posts)
    #title = jpost['post1']['title']
    #content = jpost['post1']['content']
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        add_file(title, content)
        return redirect("/")
app.run()