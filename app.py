from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Generate a URL for the 'show_post' route with post_id=1245
    post_url = url_for('show_post', post_id=1245)
    return f'Hi u, World! Go to <a href="{post_url}">Post</a>'

@app.route('/hello')
@app.route('/hello/<name>')
def greeting(name=None):
    return render_template('hello.html', name=name)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'post is: {post_id}'

if __name__ == '__main__':
    app.run(debug=True)


