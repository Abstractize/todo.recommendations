from pydantic import BaseModel
from ...utils.casing import to_camel


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
