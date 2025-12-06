from repositories.student_repository import StudentRepository
from repositories.event_repository import EventRepository
from repositories.registration_repository import RegistrationRepository

class RepositoryFactory:
    @staticmethod
    def get_repository(entity_type):
        if entity_type == 'student':
            return StudentRepository()
        elif entity_type == 'event':
            return EventRepository()
        elif entity_type == 'registration':
            return RegistrationRepository()
        else:
            raise ValueError('Unknown repository type')
