from typing import Generic, TypeVar, Type, Optional, List

from app.models import BaseModel
from app.extensions import ma, db


ModelType = TypeVar('ModelType', bound=BaseModel)
SchemaType = TypeVar('SchemaType', bound=ma.Schema)

class BaseCRUDServices(Generic[ModelType,SchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model


    def get_by_id(self, id: int) -> Optional[ModelType]:
        return self.model.query.get_or_404(id)


    def get_all(self) -> List[ModelType]:
        return self.model.query.all()


    def create(self, data:dict, schema: SchemaType) -> ModelType:
        model_instance = schema.load(data)

        model_instance.save()
        return model_instance


    def update_by_id(self, id:int, data:dict, schema: SchemaType,\
        partial: bool = False) -> ModelType:
        
        model_instance = self.model.query.get_or_404(id)
        model_instance = schema.load(data, instance=model_instance, partial=partial)
        model_instance.update()
        return model_instance


    def update(self, model_instance: ModelType, data: dict, schema: SchemaType, partial: bool = False) -> ModelType:
        model_instance = schema.load(data, instace=model_instance, partial = partial)

        model_instance.update()
        return model_instance


    def delete_by_id(self, id: int) -> None:
        item = self.model.query.filter_by(id=id).first_or_404()

        db.session.delete(item)
        db.session.commit()
