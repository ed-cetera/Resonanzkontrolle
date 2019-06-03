import flask


def create_app():
    app = flask.Flask('resonanzkontrolle')
    return app
