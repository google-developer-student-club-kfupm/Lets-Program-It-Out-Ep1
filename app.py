from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/lets-go/", methods=['POST'])
def calculate():
    # data = request.json
    data = {
        "current_gpa": 3.5,
        "current_hours": 100,
        "courses": [3, 3, 4, 4] # 14 hours
    }
    return jsonify(data)