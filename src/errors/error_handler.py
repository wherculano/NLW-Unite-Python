from src.http_types.http_response import HttpResponse

from .error_types.http_404_not_found import HttpNotFoundError
from .error_types.http_409_conflict import HttpConflictError


def http_handler(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpConflictError, HttpNotFoundError)):
        return HttpResponse(
            body={
                "errors": [
                    {
                        "title": error.name,
                        "detail": error.message,
                    }
                ]
            },
            status_code=error.status_code,
        )
    return HttpResponse(
        body={
            "errors": [
                {
                    "title": "error",
                    "detail": str(error),
                }
            ]
        },
        status_code=504,
    )
