class AppException(Exception):
    def __init__(self, error, http_code):
        # Now for your custom code...
        self.error = error
        self.http_code = http_code


class MissingFieldException(AppException):
    def __init__(self, error=None):
        super().__init__('Missing ' + error, 400)


class AuthorizationException(AppException):
    def __init__(self, error=None):
        super().__init__(error, 403)


class NotFoundException(AppException):
    def __init__(self, error=None):
        super().__init__(error, 404)


class ConflictException(AppException):
    def __init__(self, error=None):
        super().__init__(error, 409)


class ServerException(AppException):
    def __init__(self, error=None):
        super().__init__(error, 500)


class IntegrityException(AppException):
    def __init__(self, error=None):
        super().__init__('Missing ' + error, 405)
