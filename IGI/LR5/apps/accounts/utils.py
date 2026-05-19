from django.http import HttpResponseNotFound


def employee_required(view_func):

    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseNotFound('<h2>Login required</h2>')

        if (request.user.profile.role != 'employee' and not request.user.is_superuser):
            return HttpResponseNotFound('<h2>Access denied</h2>')

        return view_func(request, *args, **kwargs)

    return wrapper