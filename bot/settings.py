import os


ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID")

STORAGE_DIR_NAME = 'storage'

CONFIGURE = {
    'count': [900, 1100, 1300],
    'intensity': [0.8, 1., 1.2],
    'style': ['viridis', 'plasma', 'gray', 'binary', 'seismic', 'gnuplot']
}

DEFAULT_CONFIG = {
    'count': None,
    'intensity': 1,
    'style': 'plasma'
}
