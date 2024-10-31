from os import environ


SESSION_CONFIGS = [
    dict(
        name='survey', app_sequence=['survey'], num_demo_participants=4, 
        payment = 50
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ["treatment", "progress", "part_of_main_sample", "totalsteps"]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
# Add German to the list of supported languages
LANGUAGES = [
    ('de', 'German'),
    ('en', 'English'),
    # Add any other languages you want to support
]

# Set German as the default language
LANGUAGE_CODE = 'de'

# Activate internationalization
USE_I18N = True
USE_L10N = True

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'

USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '1147464622746'

INSTALLED_APPS = ['otree', 'django_crispy_forms', 'crispy_forms', 'crispy_bootstrap5']

CRISPY_TEMPLATE_PACK = 'bootstrap5' # or 'bootstrap4', 'foundation', etc.
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

