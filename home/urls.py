from django.conf.urls import url

from home import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    url(r'^.*\.html', views.bw_html, name='bw'),

    # The home page
    url(r'^$', views.index, name='index'),
]


