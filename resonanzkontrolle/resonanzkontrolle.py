import configparser
import secrets

import flask


def load_config(configfile=None):
    configfile_parser = configparser.ConfigParser()
    if configfile is not None:
        configfile_parser.read(configfile)
    config = {}
    config['hostname'] = configfile_parser.get(
        'Resonanzkontrolle', 'hostname', fallback=''
    )
    config['data_dir'] = configfile_parser.get(
        'Resonanzkontrolle', 'data_dir', fallback='data'
    )
    config['secret_key'] = configfile_parser.get(
        'Resonanzkontrolle', 'secret_key', fallback=secrets.token_bytes(32)
    )
    config['host'] = configfile_parser.get(
        'Resonanzkontrolle', 'host', fallback='localhost'
    )
    config['port'] = configfile_parser.getint(
        'Resonanzkontrolle', 'port', fallback=8002
    )
    return config


def create_app(config):
    app = flask.Flask('resonanzkontrolle')
    app.config['HOSTNAME'] = config['hostname']
    app.config['DATA_DIR'] = config['data_dir']
    app.config['SECRET_KEY'] = config['secret_key']
    return app
