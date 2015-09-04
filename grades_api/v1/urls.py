"""
Defines the URL routes for this app.
"""

from django.conf import settings
from django.conf.urls import patterns, url

from . import views

COURSE_ID_PATTERN = settings.COURSE_ID_PATTERN

urlpatterns = patterns(  # pylint: disable=invalid-name
    '',
    url(
        r'^grades/{}$'.format(COURSE_ID_PATTERN),
        views.GradesView.as_view(),
        name='grades_api'
    )
)
