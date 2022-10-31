from app.area.model import Area
from app.area.schema import AreaSchema
from app.services import BaseCRUDServices


class AreaServices(BaseCRUDServices[Area, AreaSchema]):
    pass


area_services = AreaServices(Area)