import Pyro4
from services import enrollment_service, student_service
from cerberus import Validator

@Pyro4.expose
class GradesManager:

    def __init__(self) -> None:
        self.validator = Validator()

    def createEnrollment(self, enrollment):
        is_valid = self.validator.validate(enrollment)

        if is_valid:
            created_enrollment = enrollment_service.create_enrollment(enrollment)
        else:
            print(self.validator.errors)


if __name__ == "__main__":
    deamon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri= deamon.register(GradesManager)
    