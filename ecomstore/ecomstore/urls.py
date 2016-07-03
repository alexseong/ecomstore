from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ecomstore.views.catalog', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^catalog/$', 'ecomstore.views.catalog'),
    url(r'^catalog/$', 'preview.views.home'),
#    url(r'^', include( 'catalog.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': '/home/alex/ecomstore/static'}),
)
