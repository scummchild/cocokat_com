import os
from pathlib import Path
import sys

from flask import Flask

# folder = Path(__file__).parent
# sys.path.insert(0, folder)
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
app = Flask(__name__)

def main():
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    from cocokat_com.views import home_views
    app.register_blueprint(home_views.blueprint)



if __name__ == '__main__':
    main()
else:
    register_blueprints()