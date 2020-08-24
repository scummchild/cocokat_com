from cocokat_com.services import comic_service
from cocokat_com.viewmodels.shared.viewmodelbase import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()

        self.comic = comic_service.get_comic_by_name(name='Cloud Toast')
        self.panels = self.comic.panels
