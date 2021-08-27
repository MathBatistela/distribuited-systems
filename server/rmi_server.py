import Pyro4
from services import enrollment_service, student_service
from cerberus import Validator
import schemas.cerberus_schemas as schemas
from sqlalchemy.exc import SQLAlchemyError

@Pyro4.expose
class GradesManager:

    def __init__(self) -> None:
        self.validator = Validator()

    @classmethod
    def raise_error(cls, message):
        return None, message

    def create_enrollment(self, enrollment):
        is_valid = self.validator.validate(enrollment, schemas.enrollment_create_schema)

        if is_valid:
            try:
                created_enrollment = enrollment_service.create_enrollment(enrollment)
            except SQLAlchemyError as e:
                return self.raise_error(str(e))

            return created_enrollment, None
        else:
            return self.raise_error(str(self.validator.errors).strip("{}"))

    def get_enrollment(self, enrollment_pk):
        is_valid = self.validator.validate(enrollment_pk, schemas.enrollment_pk_schema)

        if is_valid:
            try:
                enrollment = enrollment_service.get_enrollment(**enrollment_pk)
            except SQLAlchemyError as e:
                print(e)
                return self.raise_error(str(e))

            return enrollment, None
        else:
            return self.raise_error(str(self.validator.errors).strip("{}"))

    def update_enrollment(self, enrollment):
        is_valid = self.validator.validate(enrollment, schemas.enrollment_update_schema)
        if is_valid:
            try:
                updated_enrollment = enrollment_service.update_enrollment(enrollment)
            except SQLAlchemyError as e:
                return self.raise_error(str(e))

            return updated_enrollment, None
        else:
            return self.raise_error(str(self.validator.errors).strip("{}"))

    def delete_enrollment(self, enrollment_pk):
        is_valid = self.validator.validate(enrollment_pk, schemas.enrollment_pk_schema)
        if is_valid:
            try:
                enrollment_service.remove_enrollment(**enrollment_pk)
            except SQLAlchemyError as e:
                return self.raise_error(str(e))

            return "Enrollment deleted" , None
        else:
            return self.raise_error(str(self.validator.errors).strip("{}"))

    def get_abscenses_and_grades_by_subject(self, search):
        is_valid = self.validator.validate(search, schemas.enrollment_query_schema)
        if is_valid:
            try:
                enrollments = enrollment_service.get_enrollments(search)

                # sum all the abscenses
                abscenses = sum([enrollment["abscenses"] for enrollment in enrollments])

                # generate a grades list
                grades = [enrollment["grade"] for enrollment in enrollments]

            except SQLAlchemyError as e:
                return self.raise_error(str(e))

            return {"abscenses": abscenses, "grades": grades} , None
        else:
            return self.raise_error(str(self.validator.errors).strip("{}"))

    def get_students_by_subject(self, search):
        is_valid = self.validator.validate(search, schemas.enrolled_students_query_schema)
        if is_valid:
            try:
                students = student_service.get_students_by_enrollment(search)
            except SQLAlchemyError as e:
                return self.raise_error(str(e))

            return students , None
        else:
            return self.raise_error(str(self.validator.errors).strip("{}"))


if __name__ == "__main__":
    deamon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri= deamon.register(GradesManager)
    ns.register("rmi.gradesmanager", uri)

    print("Ready!")

    deamon.requestLoop()
    