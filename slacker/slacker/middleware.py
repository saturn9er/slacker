from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse

class AuthRequiredMiddleware(MiddlewareMixin):

    login_url = reverse('login')
    allowed_urls = [login_url]

    def process_request(self, request):

        #figuring out whether user is trying to acess allowed urls
        if request.path in self.allowed_urls:
            return None

        # redirect to login page if not authentificated 
        if not request.user.is_authenticated:
            return HttpResponseRedirect(self.login_url)

        return None