class TodoistException(Exception):
    pass


class ApiInitializationException(Exception):
    pass


class ProjectCreationException(TodoistException):
    pass


class ProjectNotFoundException(TodoistException):
    pass
