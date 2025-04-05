from flask import Flask, jsonify, request
app = Flask(__name__)

# Liste d'étudiants
students = [
    {"id": 1, "name": "Nada", "age": 22},
    {"id": 2, "name": "Farah", "age": 22},
]

# Route pour obtenir tous les étudiants
@app.route('/students', methods=['GET'])
def get_students():
#Retourne la liste de tous les étudiants.
    return jsonify(students)

# Route pour ajouter un nouvel étudiant
@app.route('/students', methods=['POST'])
def add_student():
#Ajoute un nouvel étudiant à la liste.
    new_student = request.json
    students.append(new_student)
    return jsonify(new_student), 201

# Route pour obtenir un étudiant par son ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
#Retourne un étudiant spécifique par son ID.
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"})

if __name__ == '__main__':
    app.run(debug=True)