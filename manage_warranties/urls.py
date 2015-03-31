from django.conf.urls import patterns, include, url
from manage_warranties import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Warranty_bank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^importers', views.importer_page, name = 'importer page'),
    url(r'^info', views.information_page, name = 'info page'),
    url(r'^receiver', views.text_receiver, name = 'Text receiver')
)