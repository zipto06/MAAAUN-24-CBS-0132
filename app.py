from flask import Flask, request, jsonify
from models import Patient, Queue

app = Flask(__name__)
patient_queue = Queue()

@app.route('/')
def home():
    return "Welcome to the Patient Queue Management System!"

@app.route('/register', methods=['POST'])
def register_patient():
    data = request.form
    patient = Patient(name=data['name'], age=data['age'], condition=data['condition'])
    patient_queue.enqueue(patient)
    return jsonify({"message": "Patient registered successfully!"}), 201

@app.route('/serve_patient', methods=['GET'])
def serve_patient():
    if patient_queue.is_empty():
        return jsonify({"message": "No patients in the queue."}), 404
    patient = patient_queue.dequeue()
    return jsonify({"name": patient.name, "age": patient.age, "condition": patient.condition})

if __name__ == '__main__':
    app.run(debug=True)