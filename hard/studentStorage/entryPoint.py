import json

from nameko.exceptions import safe_for_serialization, BadRequest
from nameko.web.handlers import HttpRequestHandler
from werkzeug import Response

from exception import UserNotFound, NoteNotFound

class HttpEntrypoint(HttpRequestHandler):
    """ Overrides `response_from_exception` so we can customize error handling.
    """

    mapped_errors = {
        BadRequest: (400, 'BAD_REQUEST'),
        UserNotFound: (404, 'PRODUCT_NOT_FOUND'),
        NoteNotFound: (404, 'ORDER_NOT_FOUND'),
    }

    def response_from_exception(self, exc):
        status_code, error_code = 500, 'UNEXPECTED_ERROR'

        if isinstance(exc, self.expected_exceptions):
            if type(exc) in self.mapped_errors:
                status_code, error_code = self.mapped_errors[type(exc)]
            else:
                status_code = 400
                error_code = 'BAD_REQUEST'

        return Response(
            json.dumps({
                'error': error_code,
                'message': safe_for_serialization(exc),
            }),
            status=status_code,
            mimetype='application/json'
        )


http = HttpEntrypoint.decorator