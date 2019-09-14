from django.http import HttpResponseRedirect
# from rest_framework.authtoken.models import
from datetime import datetime, timedelta

class TrailingSlashFixMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     token = request.META["HTTP_AUTHORIZATION"][-40:]
    #     if datetime.now() - Token.objects.filter(token=token)[0].created > timedelta(minutes=5):
    #         Token.objects.
    #
    #     return None