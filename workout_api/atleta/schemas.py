from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='João', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=23)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=72.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.73)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
 
class AtletaIn(Atleta):
    pass 
    
class AtletaOut(Atleta, OutMixin):
    pass