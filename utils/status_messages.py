STATUS_MESSAGES = {
    204: (True, "Successfully deleted."),
    404: (False, "Not found. It may not exist."),
    401: (False, "Unauthorized: Check API token or permissions."),
    403: (False, "Forbidden: You do not have access."),
    500: (False, "Server error: Something went wrong."),
}