"""
Utility methods for the Grades API
"""

from django.core.exceptions import ObjectDoesNotExist

from student.models import User    # pylint: disable=import-error

from ..errors import UserNotFound, UserNotAllowed


def get_user(requesting_user, username):
    """
    Returns the user to fetch grades for.
    """
    user = None

    if username is None:
        user = requesting_user

    if user is None:
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            raise UserNotFound

    if user.username != requesting_user.username and not requesting_user.is_staff:
        raise UserNotAllowed

    # The pre-fetching of groups is done to make auth checks not require an
    # additional DB lookup.
    user = User.objects.prefetch_related('groups').get(id=user.id)

    return user
