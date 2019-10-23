import gunicorn.app.base
from gunicorn.config import Config
import multiprocessing
import sys

def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1

def get_options_from_cli():
    parser = Config().parser()
    options = parser.parse_args(sys.argv)
    return options

def get_options():
    options = get_options_from_cli()
    options.workers = options.workers or number_of_workers()
    options.bind = options.bind or '127.0.0.1:8000'
    result = {}
    for key in options.__dict__:
        result[key] = getattr(options, key)
    return result

class StandaloneApplication(gunicorn.app.base.BaseApplication):
    """
    Custom application
    """
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in self.options.items()
                       if key in self.cfg.settings and value is not None])
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

def run(app):
    """
    run service
    """
    StandaloneApplication(app, options=get_options()).run()

if __name__ == "__main__":
    from app import app
    run(app)

