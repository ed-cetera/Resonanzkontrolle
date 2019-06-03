import os

import bjoern

import resonanzkontrolle.resonanzkontrolle as resonanzkontrolle


# Load config
for filepath in (
    os.environ.get("RESONANZKONTROLLE_CONF"),
    os.path.normpath(
        os.path.dirname(os.path.realpath(__file__)) + '/../etc'
    ) + '/resonanzkontrolle.conf'
):
    if filepath is None:
        continue
    configfile = os.path.expanduser(filepath)
    if os.path.isfile(configfile):
        config = resonanzkontrolle.load_config(configfile)
        break
else:
    config = resonanzkontrolle.load_config()


# Run WSGI server with app
app = resonanzkontrolle.create_app(config)
print(
    'Starting Resonanzkontrolle, ',
    'listening on ', config['host'], ':', config['port'], '.',
    sep=''
)
bjoern.run(app, config['host'], config['port'])
