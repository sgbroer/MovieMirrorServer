from flask import Flask, abort, render_template, jsonify, request
from api import make_recommendation

app = Flask('Movie_Mirror_Flask')

@app.route('/recommend', methods=['POST'])
def recommend():
    if not request.json:
        abort(400)
    data = request.json

    response = make_recommendation(data)

    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
