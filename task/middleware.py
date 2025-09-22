from inertia import share
from django.contrib import messages

class InertiaShareMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # share current user
        def auth(_request):
            if _request.user.is_authenticated:
                return {
                     'id': _request.user.id,
                     'name': _request.user.first_name if request.user.first_name else request.user.email,
                 }
            return None
        
        # share flash messages
        def flash(_request):
            storage = messages.get_messages(_request)
            return {
                'success': next((m.message for m in storage if m.level_tag == 'success'), None),
                'error': next((m.message for m in storage if m.level_tag == 'error'), None),
                'info': next((m.message for m in storage if m.level_tag == 'info'), None),
            }
        
        # Register them for this request
        share(request, auth=auth(request), flash=flash(request))

        return self.get_response(request)