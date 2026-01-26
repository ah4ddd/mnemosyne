'''defines URL pattern for accounts.'''

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    #include default auth url
    path('', include('django.contrib.auth.urls'))
]
