class Enrollment:
    def __init__(self, name, age, cpf, enrollment_id):
        self.name = name
        self.age = age
        self.cpf = cpf
        self.enrollment_id = enrollment_id
        self.status = "pending"

    def __str__(self):
        return f"Enrollment(student_name={self.name}, age={self.age}, cpf={self.cpf}, status={self.status})"

    def set_status(self, status):
        self.status = status
