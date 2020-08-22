import os
import pickle
from pathlib import Path

from bot.settings import DEFAULT_CONFIG


def create_config(chat_id):
    directory = os.path.join(os.getcwd(), 'storage', str(chat_id))
    Path(directory).mkdir(parents=True, exist_ok=True)
    path_config = os.path.join(directory, 'config.pickle')
    with open(path_config, 'wb') as handle:
        pickle.dump(DEFAULT_CONFIG, handle, protocol=pickle.HIGHEST_PROTOCOL)


def update_config(chat_id, callback_data=None):
    directory = os.path.join(os.getcwd(), 'storage', str(chat_id))
    Path(directory).mkdir(parents=True, exist_ok=True)
    path_config = os.path.join(directory, 'config.pickle')
    with open(path_config, 'rb') as handle:
        config = pickle.load(handle)
    if callback_data:
        config.update(eval(callback_data))
        with open(path_config, 'wb') as handle:
            pickle.dump(config, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return config


def create_directory_if_not_exists(chat_id):
    directory = os.path.join(os.getcwd(), 'storage', str(chat_id))
    Path(directory).mkdir(parents=True, exist_ok=True)
    return directory
