from django.conf.urls import url
from yugswebsite.views import index,contact,signup_page,signup,login,logout,addtokart,addtowishlist
from yugswebsite.views import showwishlist,showkart,redirect_to_login_modal
import django
import yugswebsite.settings
urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^index/', index,name="index"),
    url(r'^contact$', contact,name="contact"),
    url(r'^signuppage$', signup_page,name="signuppage"),
    url(r'^signup$', signup,name="signup"),
    url(r'^login$', login,name="login"),
    url(r'^logout$', logout,name="logout"),
    url(r'^addtokart$', addtokart,name="addtokart"),
    url(r'^addtowishlist$', addtowishlist,name="addtowishlist"),
    url(r'^showwishlist$', showwishlist,name="showwishlist"),
    url(r'^showkart$', showkart,name="showkart"),
    url(r'^accounts/login/',redirect_to_login_modal ,name="loginform"),
    #url(r'^static/(?P<path>.*)$', django.views.static.serve,
      #           {'document_root': yugswebsite.settings.MEDIA_ROOT}),
]
