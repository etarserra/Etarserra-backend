from app.category.model import Category
from app.category.schema import CategorySchema
from app.services import BaseCRUDServices


class CategoryServices(BaseCRUDServices[Category, CategorySchema]):
    pass


category_services = CategoryServices(Category)