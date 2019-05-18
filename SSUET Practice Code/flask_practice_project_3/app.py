from flask import Flask , render_template
from data import Articles
app = Flask(__name__)

articles = Articles()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articless():
    return render_template('articles.html' , articles=articles)

@app.route('/article/<id>')
def article(id):
    return render_template('article.html' , id=id)

if __name__ == '__main__':
    app.run(debug=True , port=3000)
