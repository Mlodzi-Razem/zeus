from .prod import *  # noqa
from django.utils.translation import gettext_lazy as _

ADMIN_NAME = 'Dawid Paćkowski'
ADMIN_EMAIL = 'dpackowski@mlodzirazem.org'

ADMINS = [
    ('Dawid Paćkowski', 'dpackowski@mlodzirazem.org')
    #('KKW Młodzi Razem', 'kkw@mlodzirazem.org')
]
ELECTION_ADMINS = ADMINS
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'kkw@mlodzirazem.org'
DEFAULT_FROM_NAME = 'Cyfrowa Urna Wyborcza Bebok'
SERVER_EMAIL = '%s <%s>' % (DEFAULT_FROM_NAME, DEFAULT_FROM_EMAIL)

HELP_EMAIL_ADDRESS = 'kkw@mlodzirazem.org'
LANGUAGE_CODE = 'pl'
LANGUAGES = [('pl', _('Polish'))]