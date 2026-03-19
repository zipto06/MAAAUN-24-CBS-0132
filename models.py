import datetime

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.registration_time = datetime.datetime.utcnow()  # Timestamp for registration

    def display_info(self):
        return f'Patient Name: {self.name}, Age: {self.age}, Registered At: {self.registration_time}'

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, patient):
        self.queue.append(patient)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)