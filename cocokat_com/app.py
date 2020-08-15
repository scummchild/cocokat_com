import os
from pathlib import Path
import sys

from flask import Flask


# folder = Path(__file__).parent
# sys.path.insert(0, folder)
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
app = Flask(__name__)

from cocokat_com.nosql import mongo_setup

def main():
    configure()
    app.run(debug=True)

def configure():
    print("Configuring Flask app:")

    register_blueprints()
    print("Registered blueprints")

    mongo_setup.global_init()
    print("DB setup completed.")
    print("", flush=True)


def register_blueprints():
    from cocokat_com.views import home_views
    app.register_blueprint(home_views.blueprint)



if __name__ == '__main__':
    main()
else:
    configure()