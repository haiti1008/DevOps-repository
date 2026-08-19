from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}
next_id = 1


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values())), 200


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = students.get(student_id)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404


@app.route('/students', methods=['POST'])
def add_student():
    global next_id
    name   = request.form.get('name')
    email  = request.form.get('email')
    course = request.form.get('course')

    if not name or not email or not course:
        return jsonify({"error": "name, email and course are required"}), 400

    student = {"id": next_id, "name": name, "email": email, "course": course}
    students[next_id] = student
    next_id += 1
    return jsonify(student), 201


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    if request.form.get('name'):   student['name']   = request.form.get('name')
    if request.form.get('email'):  student['email']  = request.form.get('email')
    if request.form.get('course'): student['course'] = request.form.get('course')

    return jsonify(student), 200


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = students.pop(student_id, None)
    if student:
        return jsonify({"message": f"Student {student_id} deleted"}), 200
    return jsonify({"error": "Student not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

