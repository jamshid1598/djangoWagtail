from proroot.settings.base import *



# Override evreything here


INSTALLED_APPS += [
    # Wagtail configuration
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    
    'modelcluster',
    'taggit',
    
    # local apps
    'apps.blog.apps.BlogConfig',
    
]

# wagtail middleware
MIDDLEWARE += [
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

# wagtail site name
WAGTAIL_SITE_NAME = "Django Wagtail Admin"

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static_root/'

static_files = BASE_DIR / 'static/'
STATICFILES_DIRS = [
    static_files,
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media_root/'
