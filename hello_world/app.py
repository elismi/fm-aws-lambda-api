from flask import (Flask, jsonify)

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify(status=200, message='Hello Flask!')


@app.route('/yolo')
def yolo():
    return jsonify(status=200, message='Yolo Flask!')


if __name__ == '__main__':
    app.run(debug=True)