"""
Errors thrown by the grades api.
"""


class GradesAPIRequestError(Exception):
    """There was a problem with the request to the Grades API. """
    pass


class UserNotFound(GradesAPIRequestError):
    """The requested user does not exist. """
    pass


class UserNotAllowed(GradesAPIRequestError):
    """The requested user was not allowed to request the grades"""
    pass
