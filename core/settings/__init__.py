from core.settings.common import *


LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_false':{
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    
}