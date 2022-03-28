from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.contrib import messages


class EditLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an organisor."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request,"You have no permission to access this page, please login")
            return redirect("user:sign_in")
        return super().dispatch(request, *args, **kwargs)

class AdminLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an organisor."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.warning(request,"You have no permission to do this")
            return redirect(request.META.get('HTTP_REFERER'))
        return super().dispatch(request, *args, **kwargs)



