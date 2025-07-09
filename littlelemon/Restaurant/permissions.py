from rest_framework.permissions import BasePermission


class IsVisitorForPostOnly(BasePermission):
    """
    Only managers can view the list (GET),
    others can only create (POST).
    """

    def has_permission(self, request, view):
        # Allow anyone to create new data
        if request.method == "POST":
            return request.user

        # Only Managers can view the list
        if request.method == "GET":
            return request.user and request.user.is_authenticated

        # Reject other methods
        return False
