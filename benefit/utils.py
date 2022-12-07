import json
from werkzeug.wrappers import Response

def validate_request_body(request, request_body):
    for field in request_body:
        if field not in request.json:
            return Response(
                json.dumps({
                    'status': 'error',
                    'message': 'Missing required field: {}'.format(field)
                }),
                status=400,
                mimetype='application/json'
            )
        elif not request.json[field]:
            return Response(
                json.dumps({
                    'status': 'error',
                    'message': '{} cannot be empty'.format(field)
                }),
                status=400,
                mimetype='application/json'
            )
