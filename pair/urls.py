from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

# App imports
from account import views as account_views
from event import views as event_views
from category import views as category_views

urlpatterns = [
	url(r'^$', event_views.index, name='index'),
	url(r'^signup/$', account_views.signup, name='signup'),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^profile/$', account_views.profile, name='profile'),
    url(r'^event/create/$', event_views.make_event, name='create event'),
    url(r'^event/(?P<pk>\d+)/$', event_views.view_event, name='view event'),
    url(r'^event/going/(?P<pk>\d+)/$', event_views.going_to_event, name='going to event'),
    url(r'^categories/$', category_views.index, name='categories'),
    url(r'^categories/(?P<pk>\d+)/$', category_views.view_category, name='view category'),
	url(r'^admin/', admin.site.urls),

]
