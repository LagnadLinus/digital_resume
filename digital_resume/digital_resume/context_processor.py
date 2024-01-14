

from django.contrib.auth.models import User     # We will be importing the user model here later, right now its built-in


def project_context(request):
    context = {
        'me': User.objects.first(),     # adding keyword argument to the context processor

    }

    return context
