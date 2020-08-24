import flask

from cocokat_com.infrastructure.view_modifiers import response
from cocokat_com.viewmodels.home.index_viewmodel import IndexViewModel

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@blueprint.route('/index')
@blueprint.route('/home')
@response(template_file='home/index.html')
def index():
    vm = IndexViewModel()
    return vm.to_dict()
