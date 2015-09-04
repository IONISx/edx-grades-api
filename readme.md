# edx-grades-api

[![Circle CI](https://circleci.com/gh/IONISx/edx-grades-api.svg?style=svg)](https://circleci.com/gh/IONISx/edx-grades-api)
[![Requirements Status](https://requires.io/github/IONISx/edx-grades-api/requirements.svg?branch=master)](https://requires.io/github/IONISx/edx-grades-api/requirements/?branch=master)

> Grades REST Api for Open edX

## How to install

### Register the application

Add the application to `INSTALLED_APPS` setting :

```python
INSTALLED_APPS = (
    ...
    'grades_api',
    ...
)
```

### URLs entries

Add URLs entries:

```python
urlpatterns = patterns('',
    ...
    url('^api/grades_api/', include('grades_api.urls', namespace='grades_api'))
    ...
)
```


## How to use

### Exposed routes

#### `/api/grades_api/v1/grades/{course_id}`

Retrieves the grade for the authenticated user for the course identified by `course_id`.

Example request:

```
GET /api/grades_api/v1/grades/org/num/rev
{
  "username": "staff",
  "course_id": "org/num/rev",
  "percentage": 0.67
}
```

#### `/api/grades_api/v1/grades/{course_id}?username={username}`

Retrieves the grade for the user matching the `username` for the course identified by `course_id`.

The requesting user has to either be `is_staff` or `username`.

## License

[AGPL](https://en.wikipedia.org/wiki/Affero_General_Public_License).
