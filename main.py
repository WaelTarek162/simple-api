from flask import Flask, render_template, request, make_response, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello wael'


@app.route('/page1')
def page1():
    return 'hello page1'


@app.route('/html')
def get_html():
    return render_template('index.html')


@app.route('/qs')
def get_qs():
    if request.args:
        req = request.args
        return " ".join(f"{k}:{v}" for k, v in req.items())
    return 'No query'


if __name__ == '__main__':
    app.run(debug=True)
