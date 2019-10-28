from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    return render(request, 'index.jinja', {'foo': 'Bar'})


class Login(LoginView):
    title = 'Login'
    template_name = 'login.jinja'
    redirect_authenticated_user = True

    def get_redirect_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        return super().get_context_data(title=self.title, **kwargs)


login = Login.as_view()
