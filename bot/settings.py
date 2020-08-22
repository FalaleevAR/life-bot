import os


ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID")

CONFIGURE = {
    'count': [800, 1000, 1300, None],
    'intensity': [0.8, 1., 1.2],
    'style': ['viridis', 'plasma', 'gray', 'binary', 'seismic', 'gnuplot']
}

DEFAULT_CONFIG = {
    'count': None,
    'intensity': 1,
    'style': 'plasma'
}
