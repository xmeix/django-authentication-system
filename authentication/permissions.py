# from rest_framework import permissions

# class HasRolePermission(permissions.BasePermission):
#     """
#     Custom permission to check if the user has a specific role.
#     """

#     def has_permission(self, request, view):
#         # Check if the user is authenticated
#         if not request.user.is_authenticated:
#             return False

#         # Check if the user has the required role (e.g., 'ADM')
#         required_role = 'ADM'  # Replace with the role you want to check
#         return request.user.role == required_role


