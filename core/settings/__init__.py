from core.settings import *


LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_false':{
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    
}