from django.contrib.auth.mixins import AccessMixin
from django.utils.translation import gettext_lazy as _


class PermissionRequiredMixin(AccessMixin):
    """
    A mixin that checks if the user has the specified permissions.
    It checks permissions before rendering the view.
    """
    permission_required = None  # permission(s) required to access the view

    def get_permission_required(self):
        if self.permission_required is None:
            raise AttributeError(
                f"{self.__class__.__name__} is missing the permission_required attribute."
            )
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms

    def has_permission(self):
        perms = self.get_permission_required()
        return self.request.user.has_perms(perms)

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
