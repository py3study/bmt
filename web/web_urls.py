from django.conf.urls import url,include
from web.views import index
app_name = 'web'

urlpatterns = [
    url(r'^$', index.index,name="index"),
    url(r'^index/', index.index,name="index"),
    url(r'^default/', index.default,name="default"),
    url(r'^user_list/', index.user_list,name="user_list"),
]