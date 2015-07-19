from courseware import grades
from courseware.courses import get_course_with_access

from opaque_keys.edx.locations import SlashSeparatedCourseKey

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from util.authentication import (
    SessionAuthenticationAllowInactiveUser,
    OAuth2AuthenticationAllowInactiveUser
)
from openedx.core.lib.api.parsers import MergePatchParser

from ..errors import UserNotFound, UserNotAllowed
from .api import get_user


class GradesView(APIView):
    """
        **Use Cases**
            Get a user's grades for a given course.
        **Example Requests**
            GET /api/grades_api/v0/grades/{course_id}?username={username}
        **Response Values for GET**
            If no user exists with the specified username, an HTTP 404 "Not
            Found" response is returned.
            If no course exists with the specified course_id, an HTTP 404 "Not
            Found" response is returned.
            If the user makes the request for her own account, or makes a
            request for another account and has "is_staff" access, an HTTP 200
            "OK" response is returned.
    """
    authentication_classes = (
        OAuth2AuthenticationAllowInactiveUser,
        SessionAuthenticationAllowInactiveUser
    )
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MergePatchParser,)

    def get(self, request, course_id):
        """
        GET /api/grades_api/v1/grades/{course_id}?username={username}
        """

        course_key = SlashSeparatedCourseKey.from_deprecated_string(course_id)
        username = request.QUERY_PARAMS.get('username')

        try:
            user = get_user(request.user, username)
        except UserNotFound:
            return Response({
                'error': 'No such user "{}"'.format(username)
            }, status=status.HTTP_404_NOT_FOUND)
        except UserNotAllowed:
            return Response({
                'error': 'Not allowed to retrieve grades for "{}"'.format(username)
            }, status=status.HTTP_403_FORBIDDEN)

        course = get_course_with_access(user, 'load', course_key, depth=None)
        grade_summary = grades.grade(user, request, course)

        return Response({
            'username': user.username,
            'course_id': course_id,
            'percent': grade_summary.get('percent')
        })
