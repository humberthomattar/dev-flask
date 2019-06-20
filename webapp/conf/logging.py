import logging
import datetime


filename = './logs/%s.log' % (
    datetime.datetime.now().strftime('-%Y-%m-%d-%Hh%Mm%Ss')
    )

logging_config = dict(
    version=1,
    formatters={
        'standard': {
                     'format':'%(asctime)s - %(name)s - %(levelname)s  { \
                         modulo: %(module)s linha: %(lineno)d} %(message)s'
            }
    },                      
    handlers={
        'file': {'class': 'logging.handlers.RotatingFileHandler',
              'filename': filename,
              'maxBytes': 1024 * 1024 * 5,
              'backupCount': 5,
              'level': 'DEBUG',
              'formatter': 'standard',
              'encoding': 'utf8'},
    
        'stream': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
            }
        },
    loggers= {
        'app': {
            'handlers': ['file', 'stream'],
            'level': logging.DEBUG,
            'propogate': 'no'
        }
    },
)