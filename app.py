from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
BLOG_DIR = 'blog'


flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html')


@app.route("/blog")
def blog():
    blog = [p for p in flatpages if p.path.startswith(BLOG_DIR)]
    blog.sort(key=lambda item: item['date'], reverse=False)
    return render_template('blog.html', blog=blog)


@app.route('/blog/<name>/')
def post(name):
    path = '{}/{}'.format(BLOG_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)

