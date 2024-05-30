import time
from pymongo import MongoClient
from app.config import settings
from app.entities.enrollment import Enrollment

class EnrollmentQueue:
    def __init__(self):
        self.client = MongoClient(settings.MONGO_URI)
        self.db = self.client[settings.DATABASE_NAME]
        self.collection = self.db["enrollments"]

    def add_enrollment(self, enrollment: Enrollment) -> str:
        enrollment_data = {
            "name": enrollment.name,
            "age": enrollment.age,
            "cpf": enrollment.cpf,
            "status": "pending",
        }
        result = self.collection.insert_one(enrollment_data)
        return str(result.inserted_id)

    def process_enrollments(self):
        while True:
            pending_enrollment = self.collection.find_one_and_update(
                {"status": "pending"},
                {"$set": {"status": "processing"}},
                return_document=True
            )
            if pending_enrollment:
                time.sleep(2)
                self.collection.update_one(
                    {"_id": pending_enrollment["_id"]},
                    {"$set": {"status": "completed"}}
                )
            else:
                time.sleep(1)

    def stop_processing(self):
        self.client.close()
