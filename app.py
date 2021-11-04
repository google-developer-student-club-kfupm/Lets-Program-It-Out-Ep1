from flask import Flask, jsonify, request
from algorithm import get_possibilties

app = Flask(__name__)
@app.route("/lets-go/", methods=['POST'])
def calculate():
    data = request.json
    current_gpa =  data.get('current_gpa')
    current_hours = data.get('current_hours')
    courses = data.get('courses')
    data = get_possibilties(courses, current_hours, current_gpa)
    return jsonify(data)